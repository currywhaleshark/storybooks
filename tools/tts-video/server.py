from __future__ import annotations

import importlib.util
import base64
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_DIR = Path(__file__).resolve().parent / "public"
SERIES_DIR = REPO_ROOT / "series"
RUNTIME_DIR = Path(__file__).resolve().parent / "runtime"
RENDERER_PATH = (
    REPO_ROOT
    / "series"
    / "sherlock-fin-deep-city"
    / "videos"
    / "누가_먼저_왔을까_tts_google"
    / "make_tts_video.py"
)
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
EXCLUDED_DIRS = {"audio", "segments", "work", "drafts", "rejected", "print-output"}
TTS_PRESET_FILENAME = "tts_voice_presets.yaml"
JOBS: dict[str, dict[str, object]] = {}


def load_renderer():
    spec = importlib.util.spec_from_file_location("tts_video_renderer", RENDERER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load renderer: {RENDERER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RENDERER = load_renderer()


def is_inside(parent: Path, child: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def repo_path(relative_path: str | None) -> Path:
    resolved = (REPO_ROOT / (relative_path or "")).resolve()
    if not is_inside(REPO_ROOT, resolved):
        raise RuntimeError("저장소 밖의 경로는 사용할 수 없습니다.")
    return resolved


def to_repo_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def describe_exception(exc: Exception) -> str:
    message = str(exc)
    if message:
        return message
    return f"{type(exc).__name__}: {exc!r}"


def renderer_python_executable() -> str:
    local_roots = []
    if os.environ.get("LOCALAPPDATA"):
        local_roots.append(Path(str(os.environ["LOCALAPPDATA"])))
    if os.environ.get("USERPROFILE"):
        local_roots.append(Path(str(os.environ["USERPROFILE"])) / "AppData" / "Local")
    local_roots.append(Path.home() / "AppData" / "Local")

    for local_root in local_roots:
        gcloud_python = local_root / "Google" / "Cloud SDK" / "google-cloud-sdk" / "platform" / "bundledpython" / "python.exe"
        if gcloud_python.exists():
            return str(gcloud_python)
    return sys.executable


def leading_number(path: Path) -> int | None:
    match = re.match(r"^(\d+)", path.name)
    return int(match.group(1)) if match else None


def sorted_images(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    images = [
        path
        for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS and leading_number(path) is not None
    ]
    return sorted(images, key=lambda path: (leading_number(path) if leading_number(path) is not None else 999999, path.name))


def series_root_for_episode_folder(folder: Path) -> Path | None:
    parts = folder.resolve().parts
    if "images" not in parts:
        return None
    index = len(parts) - 1 - list(reversed(parts)).index("images")
    if index <= 0:
        return None
    return Path(*parts[:index])


def script_candidates(series_root: Path, episode_title: str) -> list[dict[str, object]]:
    docs_episode_dir = series_root / "docs" / "episodes"
    if not docs_episode_dir.exists():
        return []
    normalized_title = normalize_match_text(episode_title)
    candidates = []
    for path in docs_episode_dir.glob("*.md"):
        normalized_name = normalize_match_text(path.stem)
        normalized_content = normalize_match_text(path.read_text(encoding="utf-8", errors="ignore")[:2000])
        likely = (
            normalized_title in normalized_name
            or normalized_name in normalized_title
            or normalized_title in normalized_content
        )
        candidates.append(
            {
                "path": to_repo_path(path),
                "name": path.name,
                "likely": likely,
            }
        )
    likely_candidates = [item for item in candidates if item["likely"]]
    if likely_candidates:
        candidates = likely_candidates
    return sorted(candidates, key=lambda item: (not item["likely"], not is_tts_script_name(str(item["name"])), str(item["name"])))


def normalize_match_text(text: str) -> str:
    return re.sub(r"[^0-9a-z가-힣]+", "", text.lower())


def is_tts_script_name(name: str) -> bool:
    return re.search(r"(?:^|[_-])tts(?:[_-]|\.|$)", name, flags=re.I) is not None


def parse_preset_value(value: str) -> object:
    value = value.strip()
    if not value:
        return ""
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [strip_preset_quotes(part.strip()) for part in inner.split(",")]
    return strip_preset_quotes(value)


def strip_preset_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def load_tts_voice_presets(series_root: Path | None) -> dict[str, object] | None:
    if not series_root:
        return None
    preset_path = series_root / "docs" / TTS_PRESET_FILENAME
    if not preset_path.exists():
        return None

    data: dict[str, object] = {}
    current_section = ""
    current_character = ""
    current_list_key = ""
    for raw_line in preset_path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0:
            key, _, raw_value = line.partition(":")
            if raw_value.strip():
                data[key] = parse_preset_value(raw_value)
                current_section = ""
            else:
                data[key] = {}
                current_section = key
            current_character = ""
            current_list_key = ""
            continue

        if current_section == "audioTagPolicy" and indent == 2:
            key, _, raw_value = line.partition(":")
            policy = data.setdefault("audioTagPolicy", {})
            if isinstance(policy, dict):
                policy[key] = parse_preset_value(raw_value)
            continue

        if current_section != "characters":
            continue

        characters = data.setdefault("characters", {})
        if not isinstance(characters, dict):
            continue

        if indent == 2 and line.endswith(":"):
            current_character = line[:-1]
            characters[current_character] = {}
            current_list_key = ""
            continue

        if not current_character:
            continue

        character = characters.get(current_character)
        if not isinstance(character, dict):
            continue

        if indent == 4:
            key, _, raw_value = line.partition(":")
            if raw_value.strip():
                character[key] = parse_preset_value(raw_value)
                current_list_key = ""
            else:
                character[key] = []
                current_list_key = key
            continue

        if indent == 6 and current_list_key and line.startswith("- "):
            list_value = character.setdefault(current_list_key, [])
            if isinstance(list_value, list):
                list_value.append(parse_preset_value(line[2:]))

    return data


def tts_voice_presets_for_episode_folder(final_folder: str | None) -> dict[str, object] | None:
    folder = repo_path(final_folder)
    return load_tts_voice_presets(series_root_for_episode_folder(folder))


def discover_book_folder(folder: Path) -> dict[str, object] | None:
    images = sorted_images(folder)
    if not images:
        return None
    has_cover = any((leading_number(path) == 0) for path in images)
    has_body = any((leading_number(path) or 0) > 0 for path in images)
    if not has_cover and not has_body:
        return None

    series_root = series_root_for_episode_folder(folder)
    episode_folder = folder.parent if folder.name == "final" else folder
    episode_title = episode_folder.name
    return {
        "id": to_repo_path(folder),
        "title": episode_title,
        "series": series_root.name if series_root else "",
        "finalFolder": to_repo_path(folder),
        "imageCount": len(images),
        "images": [to_repo_path(path) for path in images],
        "scripts": script_candidates(series_root, episode_title) if series_root else [],
        "defaultOutputDir": to_repo_path((series_root or REPO_ROOT) / "videos" / f"{episode_title}_tts_app"),
    }


def find_book_folders(folder: Path, depth: int = 0) -> list[dict[str, object]]:
    if not folder.exists() or depth > 7:
        return []
    current = discover_book_folder(folder)
    found = [current] if current else []
    for child in folder.iterdir():
        if not child.is_dir():
            continue
        if child.name in EXCLUDED_DIRS:
            continue
        if re.match(r"^batch(?:_|$)", child.name, flags=re.I):
            continue
        if current and child.name == "final":
            continue
        found.extend(find_book_folders(child, depth + 1))
    return found


def clean_extracted_text(text: str) -> str:
    result = text.strip().replace("\r\n", "\n")
    result = re.sub(r'^["“]+', "", result)
    result = re.sub(r'["”]+$', "", result)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def extract_text_blocks(markdown: str) -> list[str]:
    patterns = [
        r"(?:표지|페이지) 안에 다음 한국어(?: 제목)? 텍스트[^\n]*:\s*```text\s*\n([\s\S]*?)```",
        r"###\s*페이지\s*텍스트[\s\S]*?```text\s*\n([\s\S]*?)```",
        r"(?:^|\n)Text:\s*\n```text\s*\n([\s\S]*?)```",
        r'(?:^|\n)Text:\s*\n(["“][\s\S]*?["”])(?=\n\s*(?:---|##|###|$))',
    ]
    for pattern in patterns:
        blocks = [clean_extracted_text(match) for match in re.findall(pattern, markdown)]
        if blocks:
            return blocks
    saved_blocks = []
    for section in re.split(r"^##\s+", markdown, flags=re.MULTILINE)[1:]:
        title, _, body = section.partition("\n")
        if Path(title.strip()).suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        text = clean_extracted_text(body)
        if text:
            saved_blocks.append(text)
    if saved_blocks:
        return saved_blocks
    return []


def build_script_markdown(title: str, images: list[str], texts: list[str]) -> str:
    lines = [f"# {title} TTS 원고", ""]
    for index, image in enumerate(images):
        lines.extend([f"## {Path(image).name}", "", texts[index].strip() if index < len(texts) else "", ""])
    return "\n".join(lines).rstrip() + "\n"


def normalize_tts_text(text: str) -> str:
    return re.sub(r"\s*[~〜～]+\s*", "... ", text).strip()


def align_texts_for_images(title: str, images: list[str], texts: list[str]) -> list[str]:
    aligned = [normalize_tts_text(str(text)) for text in texts]
    has_cover = any(Path(image).name.startswith("00") for image in images)
    if has_cover and len(aligned) == len(images) - 1:
        aligned = [title.replace("_", " "), *aligned]
    while len(aligned) < len(images):
        aligned.append("")
    if has_cover and images and Path(images[0]).name.startswith("00") and not aligned[0].strip():
        aligned[0] = title.replace("_", " ")
    return aligned


def save_script(body: dict[str, object]) -> dict[str, object]:
    episode = body["episode"]
    texts = body.get("texts") or []
    output_dir = repo_path(str(body.get("outputDir") or episode["defaultOutputDir"]))
    output_dir.mkdir(parents=True, exist_ok=True)
    images = [to_repo_path(path) for path in sorted_images(repo_path(str(episode["finalFolder"])))]
    title = str(episode["title"])
    script = build_script_markdown(title, images, align_texts_for_images(title, images, [str(text) for text in texts]))
    script_path = output_dir / "tts_script.md"
    script_path.write_text(script, encoding="utf-8")
    return {"scriptPath": to_repo_path(script_path), "outputDir": to_repo_path(output_dir), "script": script}


def output_video_path(output_dir: Path, output_name: str | None) -> Path:
    name = re.sub(r'[\\/:*?"<>|]', "_", output_name or "storybook_tts_video.mp4")
    if not name.lower().endswith(".mp4"):
        name += ".mp4"
    return output_dir / name


def leading_number_from_name(name: str) -> int | None:
    match = re.match(r"^(\d+)", name)
    return int(match.group(1)) if match else None


def sorted_audio_payload(files: list[object]) -> list[dict[str, object]]:
    indexed = [(index, file) for index, file in enumerate(files) if isinstance(file, dict)]

    def sort_key(item: tuple[int, dict[str, object]]) -> tuple[int, int, str]:
        index, file = item
        name = str(file.get("name") or "")
        number = leading_number_from_name(name)
        return (0 if number is not None else 1, number if number is not None else index, name)

    return [file for _, file in sorted(indexed, key=sort_key)]


def prepare_manual_audio(output_dir: Path, files: list[object], expected_count: int) -> None:
    audio_files = sorted_audio_payload(files)
    if len(audio_files) < expected_count:
        raise RuntimeError(f"오디오 파일이 부족합니다. 현재 {len(audio_files)}개, 필요한 파일 {expected_count}개입니다.")

    audio_dir = output_dir / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    for index, file in enumerate(audio_files[:expected_count]):
        name = Path(str(file.get("name") or f"{index:02d}.mp3")).name
        extension = Path(name).suffix.lower() or ".mp3"
        data = str(file.get("dataBase64") or "")
        if "," in data:
            data = data.split(",", 1)[1]
        try:
            audio_bytes = base64.b64decode(data, validate=True)
        except Exception as exc:
            raise RuntimeError(f"{name} 오디오 파일을 읽지 못했습니다.") from exc

        target = audio_dir / f"{index:02d}.mp3"
        if extension == ".mp3":
            target.write_bytes(audio_bytes)
            continue

        source = audio_dir / f"{index:02d}_source{extension}"
        source.write_bytes(audio_bytes)
        RENDERER.run_ffmpeg(["-y", "-i", str(source), "-vn", "-c:a", "libmp3lame", "-b:a", "192k", str(target)])


def renderer_audio(settings: dict[str, object], text: str, output: Path) -> None:
    tts = str(settings.get("tts") or "gemini")
    rate = float(settings.get("speakingRate") or 1)
    pitch = float(settings.get("pitch") or 0)
    args = [
        renderer_python_executable(),
        "-X",
        "utf8",
        str(RENDERER_PATH),
        "--tts",
        tts,
        "--speaking-rate",
        str(rate),
        "--pitch",
        str(pitch),
        "--sample-text",
        text,
        "--sample-output",
        str(output),
    ]
    if tts == "cloud":
        args.extend(["--cloud-voice", str(settings.get("cloudVoice") or "ko-KR-Chirp3-HD-Kore")])
    elif tts == "gemini":
        args.extend(
            [
                "--gemini-model",
                str(settings.get("geminiModel") or "gemini-2.5-flash-tts"),
                "--gemini-voice",
                str(settings.get("geminiVoice") or "Kore"),
                "--gemini-prompt",
                str(settings.get("geminiPrompt") or ""),
            ]
        )

    result = subprocess.run(
        args,
        cwd=REPO_ROOT,
        env=renderer_subprocess_env(),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=180,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or f"TTS process failed with exit code {result.returncode}").strip()
        raise RuntimeError(detail)


def renderer_subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    for key in list(env):
        if key.lower() == "path" and key != "PATH":
            del env[key]
    python_dir = Path(renderer_python_executable()).resolve().parent
    dll_dir = python_dir / "DLLs"
    existing_path = env.get("PATH", "")
    env["PATH"] = f"{python_dir};{dll_dir};{existing_path}" if existing_path else f"{python_dir};{dll_dir}"
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    return env


def run_renderer_process(args: list[str], timeout: int = 180) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO_ROOT,
        env=renderer_subprocess_env(),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def renderer_cloud_voices(language_code: str = "ko-KR") -> list[dict[str, object]]:
    result = run_renderer_process(
        [
            renderer_python_executable(),
            "-X",
            "utf8",
            str(RENDERER_PATH),
            "--list-cloud-voices",
            "--cloud-language",
            language_code,
        ],
        timeout=90,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or f"Voice list process failed with exit code {result.returncode}").strip()
        raise RuntimeError(detail)
    voices = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        name, gender, sample_rate, languages = (line.split("\t") + ["", "", "", ""])[:4]
        voices.append({"name": name, "gender": gender, "sampleRate": sample_rate, "languages": languages})
    return voices


def create_sample(settings: dict[str, object]) -> dict[str, str]:
    sample_dir = RUNTIME_DIR / "samples"
    sample_dir.mkdir(parents=True, exist_ok=True)
    sample_path = sample_dir / f"{uuid.uuid4()}.mp3"
    text = str(settings.get("sampleText") or "포포는 안 졸려요. 낮잠은 신나게 놀 힘을 모으는 시간이래요.")
    renderer_audio(settings, text, sample_path)
    media_path = to_repo_path(sample_path)
    return {"path": media_path, "url": f"/media?path={quote(media_path)}"}


def audio_review_item(output_dir: Path, page: dict[str, str], index: int) -> dict[str, object]:
    audio_path = output_dir / "audio" / f"{index:02d}.mp3"
    media_path = to_repo_path(audio_path)
    return {
        "index": index,
        "image": page["image"],
        "text": page["text"],
        "audioPath": media_path,
        "url": f"/media?path={quote(media_path)}&v={int(audio_path.stat().st_mtime)}",
    }


def synthesize_review_audio(output_dir: Path, pages: list[dict[str, str]], settings: dict[str, object], index: int) -> dict[str, object]:
    if index < 0 or index >= len(pages):
        raise RuntimeError("페이지 번호가 범위를 벗어났습니다.")
    if str(settings.get("tts") or "gemini") == "manual":
        raise RuntimeError("오디오 업로드 모드는 리롤 대신 파일을 다시 선택해야 합니다.")

    audio_dir = output_dir / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    audio_path = audio_dir / f"{index:02d}.mp3"
    renderer_audio(settings, pages[index]["text"], audio_path)
    return audio_review_item(output_dir, pages[index], index)


def setup_episode_render_context(episode: dict[str, object], script_path: str, output_dir: Path) -> list[dict[str, str]]:
    RENDERER.EPISODE_DIR = repo_path(str(episode["finalFolder"]))
    RENDERER.SCRIPT_PATH = repo_path(script_path)
    RENDERER.OUT_DIR = output_dir
    return RENDERER.read_script()


def run_audio_review(job: dict[str, object], body: dict[str, object]) -> None:
    try:
        episode = body["episode"]
        settings = body.get("settings") or {}
        saved = save_script(
            {
                "episode": episode,
                "texts": body.get("texts") or [],
                "outputDir": settings.get("outputDir") or episode["defaultOutputDir"],
            }
        )
        output_dir = repo_path(str(saved["outputDir"]))
        pages = setup_episode_render_context(episode, str(saved["scriptPath"]), output_dir)
        for index, _page in enumerate(pages):
            job["stdout"] = f"음성 생성 중: {index + 1} / {len(pages)}"
            synthesize_review_audio(output_dir, pages, settings, index)

        job["audioReview"] = {
            "scriptPath": saved["scriptPath"],
            "outputDir": saved["outputDir"],
            "items": [audio_review_item(output_dir, page, index) for index, page in enumerate(pages)],
        }
        job["scriptPath"] = saved["scriptPath"]
        job["status"] = "complete"
        job["stdout"] = f"음성 검수용 파일 {len(pages)}개 생성 완료"
    except Exception as exc:
        job["status"] = "failed"
        job["stderr"] = describe_exception(exc)
    finally:
        job["finishedAt"] = time.strftime("%Y-%m-%dT%H:%M:%S")


def reroll_audio(body: dict[str, object]) -> dict[str, object]:
    episode = body["episode"]
    settings = body.get("settings") or {}
    index = int(body.get("index") or 0)
    saved = save_script(
        {
            "episode": episode,
            "texts": body.get("texts") or [],
            "outputDir": settings.get("outputDir") or episode["defaultOutputDir"],
        }
    )
    output_dir = repo_path(str(saved["outputDir"]))
    pages = setup_episode_render_context(episode, str(saved["scriptPath"]), output_dir)
    return {
        "scriptPath": saved["scriptPath"],
        "outputDir": saved["outputDir"],
        "item": synthesize_review_audio(output_dir, pages, settings, index),
    }


def create_job() -> dict[str, object]:
    job_id = str(uuid.uuid4())
    job = {
        "id": job_id,
        "status": "running",
        "startedAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "finishedAt": None,
        "stdout": "",
        "stderr": "",
        "scriptPath": "",
        "outputPath": "",
    }
    JOBS[job_id] = job
    return job


def run_render(job: dict[str, object], body: dict[str, object]) -> None:
    try:
      episode = body["episode"]
      settings = body.get("settings") or {}
      tts_mode = str(settings.get("tts") or "gemini")
      saved = save_script({"episode": episode, "texts": body.get("texts") or [], "outputDir": settings.get("outputDir") or episode["defaultOutputDir"]})
      output_dir = repo_path(str(saved["outputDir"]))
      output_path = output_video_path(output_dir, str(settings.get("outputName") or "storybook_tts.mp4"))

      pages = setup_episode_render_context(episode, str(saved["scriptPath"]), output_dir)
      reuse_audio = bool(settings.get("reviewedAudio"))
      renderer_tts = tts_mode
      if tts_mode == "manual":
          prepare_manual_audio(output_dir, list(settings.get("manualAudioFiles") or []), len(pages))
          reuse_audio = True
          renderer_tts = "gemini"
      if settings.get("reviewedAudio"):
          missing = [f"{index:02d}.mp3" for index in range(len(pages)) if not (output_dir / "audio" / f"{index:02d}.mp3").exists()]
          if missing:
              raise RuntimeError(f"검수된 오디오가 없습니다: {', '.join(missing)}")
          renderer_tts = "gemini"
      segments = RENDERER.build_segments(
          pages,
          reuse_audio=reuse_audio,
          tts=renderer_tts,
          cloud_voice=str(settings.get("cloudVoice") or "ko-KR-Chirp3-HD-Kore"),
          cloud_language="ko-KR",
          gemini_model=str(settings.get("geminiModel") or "gemini-2.5-flash-tts"),
          gemini_prompt=str(settings.get("geminiPrompt") or ""),
          gemini_voice=str(settings.get("geminiVoice") or "Kore"),
          speaking_rate=float(settings.get("speakingRate") or 1),
          pitch=float(settings.get("pitch") or 0),
          page_gap=float(settings.get("pageGap") or 0.8),
          audio_tail_pad=float(settings.get("audioTailPad") or 0.35),
      )
      RENDERER.concatenate(segments, output_path)
      duration = sum(RENDERER.ffprobe_duration(segment) for segment in segments)
      job["stdout"] = f"Created: {output_path}\nDuration: {round(duration)} seconds\n"
      job["scriptPath"] = saved["scriptPath"]
      job["outputPath"] = to_repo_path(output_path)
      job["status"] = "complete"
    except Exception as exc:
      job["status"] = "failed"
      job["stderr"] = describe_exception(exc)
    finally:
      job["finishedAt"] = time.strftime("%Y-%m-%dT%H:%M:%S")


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status: int, payload: object) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self) -> dict[str, object]:
        length = int(self.headers.get("content-length") or "0")
        return json.loads(self.rfile.read(length).decode("utf-8")) if length else {}

    def serve_file(self, path: Path, content_type: str | None = None) -> None:
        if not path.exists() or not path.is_file():
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("content-type", content_type or mimetypes.guess_type(path.name)[0] or "application/octet-stream")
        self.send_header("content-length", str(path.stat().st_size))
        self.end_headers()
        with path.open("rb") as file:
            shutil.copyfileobj(file, self.wfile)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        try:
            if parsed.path == "/api/episodes":
                self.send_json(200, {"episodes": find_book_folders(SERIES_DIR)})
                return
            if parsed.path == "/api/voices":
                voices = renderer_cloud_voices(params.get("language", ["ko-KR"])[0])
                self.send_json(200, {"voices": voices})
                return
            if parsed.path == "/api/tts-presets":
                preset = tts_voice_presets_for_episode_folder(params.get("finalFolder", [""])[0])
                self.send_json(200, {"preset": preset})
                return
            if parsed.path.startswith("/api/jobs/"):
                job = JOBS.get(unquote(parsed.path.removeprefix("/api/jobs/")))
                self.send_json(200 if job else 404, {"job": job} if job else {"error": "작업을 찾을 수 없습니다."})
                return
            if parsed.path == "/image":
                self.serve_file(repo_path(params.get("path", [""])[0]))
                return
            if parsed.path == "/media":
                self.serve_file(repo_path(params.get("path", [""])[0]))
                return

            target = PUBLIC_DIR / ("index.html" if parsed.path == "/" else parsed.path.lstrip("/"))
            self.serve_file(target)
        except Exception as exc:
            self.send_json(500, {"error": describe_exception(exc)})

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        try:
            body = self.read_json()
            if parsed.path == "/api/extract":
                markdown = repo_path(str(body.get("sourcePath") or "")).read_text(encoding="utf-8")
                self.send_json(200, {"texts": extract_text_blocks(markdown)})
                return
            if parsed.path == "/api/extract-content":
                markdown = str(body.get("content") or "")
                self.send_json(200, {"texts": extract_text_blocks(markdown)})
                return
            if parsed.path == "/api/save-script":
                self.send_json(200, save_script(body))
                return
            if parsed.path == "/api/sample":
                self.send_json(200, {"sample": create_sample(body.get("settings") or {})})
                return
            if parsed.path == "/api/audio-review/start":
                job = create_job()
                threading.Thread(target=run_audio_review, args=(job, body), daemon=True).start()
                self.send_json(200, {"job": job})
                return
            if parsed.path == "/api/audio-review/reroll":
                self.send_json(200, {"audioReview": reroll_audio(body)})
                return
            if parsed.path == "/api/render":
                job = create_job()
                threading.Thread(target=run_render, args=(job, body), daemon=True).start()
                self.send_json(200, {"job": job})
                return
            self.send_json(404, {"error": "Not found"})
        except Exception as exc:
            self.send_json(500, {"error": describe_exception(exc)})


def main() -> None:
    port = int(os.environ.get("PORT", "4174"))
    server = ThreadingHTTPServer(("localhost", port), Handler)
    print(f"TTS video web tool: http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
