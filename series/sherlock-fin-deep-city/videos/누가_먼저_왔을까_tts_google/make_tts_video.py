from __future__ import annotations

import argparse
import base64
import html
import json
import math
import os
import re
import subprocess
import sys
import time
import shutil
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[4]
EPISODE_DIR = ROOT / "series" / "sherlock-fin-deep-city" / "images" / "episodes" / "누가_먼저_왔을까" / "final"
OUT_DIR = Path(__file__).resolve().parent
SCRIPT_PATH = OUT_DIR / "tts_script.md"
CLOUD_TTS_SCOPE = "https://www.googleapis.com/auth/cloud-platform"


def read_script() -> list[dict[str, str]]:
    text = SCRIPT_PATH.read_text(encoding="utf-8")
    sections = re.split(r"^##\s+", text, flags=re.MULTILINE)[1:]
    pages: list[dict[str, str]] = []
    for section in sections:
        title, body = section.split("\n", 1)
        image_name = title.strip()
        narration = re.sub(r"\n{3,}", "\n\n", body.strip())
        narration = narration.replace("\n", " ")
        narration = re.sub(r"\s+", " ", narration).strip()
        if image_name and narration:
            pages.append({"image": image_name, "text": narration})
    return pages


def split_for_google_tts(text: str, limit: int = 180) -> list[str]:
    pieces: list[str] = []
    current = ""
    for sentence in re.split(r"(?<=[.!?。！？요])\s+", text):
        sentence = sentence.strip()
        if not sentence:
            continue
        if len(current) + len(sentence) + 1 <= limit:
            current = f"{current} {sentence}".strip()
        else:
            if current:
                pieces.append(current)
            if len(sentence) <= limit:
                current = sentence
            else:
                for i in range(0, len(sentence), limit):
                    pieces.append(sentence[i : i + limit])
                current = ""
    if current:
        pieces.append(current)
    return pieces


def download_google_tts(text: str, output: Path, *, lang: str = "ko", slow: bool = False) -> None:
    parts = split_for_google_tts(text)
    temp_files: list[Path] = []
    for index, part in enumerate(parts, 1):
        query = urlencode(
            {
                "ie": "UTF-8",
                "client": "tw-ob",
                "tl": lang,
                "q": part,
                "ttsspeed": "0.82" if slow else "1",
            }
        )
        url = f"https://translate.google.com/translate_tts?{query}"
        req = Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://translate.google.com/",
            },
        )
        temp = output.with_name(f"{output.stem}_{index:02d}.mp3")
        with urlopen(req, timeout=30) as response:
            temp.write_bytes(response.read())
        temp_files.append(temp)
        time.sleep(0.15)

    if len(temp_files) == 1:
        temp_files[0].replace(output)
        return

    list_file = output.with_suffix(".concat.txt")
    list_file.write_text(
        "".join(f"file '{temp.as_posix()}'\n" for temp in temp_files),
        encoding="utf-8",
    )
    run_ffmpeg(["-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(output)])


def adc_path() -> Path:
    appdata = os.environ.get("APPDATA")
    if not appdata:
        raise RuntimeError("APPDATA is not set; cannot find gcloud ADC credentials.")
    path = Path(appdata) / "gcloud" / "application_default_credentials.json"
    if not path.exists():
        raise FileNotFoundError(
            f"ADC credentials not found at {path}. Run: gcloud auth application-default login"
        )
    return path


def read_adc() -> dict[str, str]:
    data = json.loads(adc_path().read_text(encoding="utf-8"))
    if data.get("type") != "authorized_user":
        raise RuntimeError(f"Unsupported ADC type: {data.get('type')}")
    for key in ("client_id", "client_secret", "refresh_token"):
        if not data.get(key):
            raise RuntimeError(f"ADC credentials are missing {key}.")
    return data


def cloud_access_token(adc: dict[str, str]) -> str:
    body = urlencode(
        {
            "client_id": adc["client_id"],
            "client_secret": adc["client_secret"],
            "refresh_token": adc["refresh_token"],
            "grant_type": "refresh_token",
            "scope": CLOUD_TTS_SCOPE,
        }
    ).encode("utf-8")
    req = Request(
        "https://oauth2.googleapis.com/token",
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urlopen(req, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
    if "access_token" not in data:
        raise RuntimeError(f"OAuth token response did not include access_token: {data}")
    return data["access_token"]


def cloud_headers(adc: dict[str, str]) -> dict[str, str]:
    headers = {
        "Authorization": f"Bearer {cloud_access_token(adc)}",
        "Content-Type": "application/json; charset=utf-8",
    }
    quota_project = adc.get("quota_project_id")
    if quota_project:
        headers["x-goog-user-project"] = quota_project
    return headers


def cloud_tts_request(payload: dict[str, object], *, endpoint: str = "text:synthesize") -> dict[str, object]:
    adc = read_adc()
    req = Request(
        f"https://texttospeech.googleapis.com/v1/{endpoint}",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload else None,
        headers=cloud_headers(adc),
        method="POST" if payload else "GET",
    )
    with urlopen(req, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def list_cloud_voices(language_code: str = "ko-KR") -> list[dict[str, object]]:
    adc = read_adc()
    url = f"https://texttospeech.googleapis.com/v1/voices?{urlencode({'languageCode': language_code})}"
    req = Request(url, headers=cloud_headers(adc))
    with urlopen(req, timeout=60) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data.get("voices", [])


def download_cloud_tts(
    text: str,
    output: Path,
    *,
    voice: str,
    language_code: str,
    speaking_rate: float,
    pitch: float,
    model_name: str | None = None,
    prompt: str | None = None,
) -> None:
    synthesis_input: dict[str, str] = {"text": text}
    if prompt:
        synthesis_input["prompt"] = prompt
    voice_params: dict[str, str] = {"languageCode": language_code, "name": voice}
    if model_name:
        voice_params["modelName"] = model_name
    payload = {
        "input": synthesis_input,
        "voice": voice_params,
        "audioConfig": {
            "audioEncoding": "MP3",
            "speakingRate": speaking_rate,
            "pitch": pitch,
        },
    }
    data = cloud_tts_request(payload)
    audio_content = data.get("audioContent")
    if not isinstance(audio_content, str):
        raise RuntimeError(f"Cloud TTS response did not include audioContent: {data}")
    output.write_bytes(base64.b64decode(audio_content))


def synthesize_sapi(text: str, output: Path, *, voice: str = "Microsoft Heami Desktop") -> None:
    temp_dir = OUT_DIR / "_tmp_sapi"
    temp_dir.mkdir(parents=True, exist_ok=True)
    safe_stem = re.sub(r"[^A-Za-z0-9_-]+", "_", output.stem)
    text_file = temp_dir / f"{safe_stem}.txt"
    temp_output = temp_dir / f"{safe_stem}.wav"
    ps_file = temp_dir / "sapi_speak.ps1"
    ps_file.write_text(
        "\n".join(
            [
                "param([string]$TextPath, [string]$OutPath)",
                "Add-Type -AssemblyName System.Speech",
                "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer",
                "$s.SelectVoice('Microsoft Heami Desktop')",
                "$s.Rate = -2",
                "$s.Volume = 100",
                "$text = Get-Content -LiteralPath $TextPath -Raw -Encoding UTF8",
                "$s.SetOutputToWaveFile($OutPath)",
                "$s.Speak($text)",
                "$s.Dispose()",
            ]
        ),
        encoding="utf-8",
    )
    text_file.write_text(text, encoding="utf-8")
    subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(ps_file),
            "-TextPath",
            str(text_file),
            "-OutPath",
            str(temp_output),
        ],
        check=True,
    )
    shutil.copyfile(temp_output, output)


def run_ffmpeg(args: list[str]) -> None:
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", *args]
    subprocess.run(command, check=True)


def ffprobe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    data = json.loads(result.stdout)
    return float(data["format"]["duration"])


def build_segments(
    pages: list[dict[str, str]],
    *,
    reuse_audio: bool,
    tts: str,
    cloud_voice: str,
    cloud_language: str,
    gemini_model: str,
    gemini_prompt: str,
    gemini_voice: str,
    speaking_rate: float,
    pitch: float,
    page_gap: float,
) -> list[Path]:
    audio_dir = OUT_DIR / "audio"
    segment_dir = OUT_DIR / "segments"
    audio_dir.mkdir(exist_ok=True)
    segment_dir.mkdir(exist_ok=True)
    segments: list[Path] = []

    for index, page in enumerate(pages):
        image = EPISODE_DIR / page["image"]
        if not image.exists():
            raise FileNotFoundError(image)

        audio = audio_dir / f"{index:02d}.{'wav' if tts == 'sapi' else 'mp3'}"
        if not reuse_audio or not audio.exists():
            print(f"TTS {index:02d}: {page['image']}")
            if tts == "sapi":
                synthesize_sapi(page["text"], audio)
            elif tts == "cloud":
                download_cloud_tts(
                    page["text"],
                    audio,
                    voice=cloud_voice,
                    language_code=cloud_language,
                    speaking_rate=speaking_rate,
                    pitch=pitch,
                )
            elif tts == "gemini":
                download_cloud_tts(
                    page["text"],
                    audio,
                    voice=gemini_voice,
                    language_code=cloud_language,
                    speaking_rate=speaking_rate,
                    pitch=pitch,
                    model_name=gemini_model,
                    prompt=gemini_prompt,
                )
            else:
                download_google_tts(page["text"], audio, slow=True)

        duration = max(3.0, ffprobe_duration(audio) + max(0.0, page_gap))
        segment = segment_dir / f"{index:02d}.mp4"
        vf = (
            "scale=1920:1080:force_original_aspect_ratio=decrease,"
            "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,"
            "format=yuv420p"
        )
        run_ffmpeg(
            [
                "-y",
                "-loop",
                "1",
                "-t",
                f"{duration:.3f}",
                "-i",
                str(image),
                "-i",
                str(audio),
                "-vf",
                vf,
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-tune",
                "stillimage",
                "-af",
                f"apad=pad_dur={max(0.0, page_gap):.3f}",
                "-c:a",
                "aac",
                "-b:a",
                "160k",
                "-t",
                f"{duration:.3f}",
                str(segment),
            ]
        )
        segments.append(segment)
    return segments


def concatenate(segments: list[Path], output: Path) -> None:
    list_file = OUT_DIR / "segments.txt"
    list_file.write_text("".join(f"file '{path.as_posix()}'\n" for path in segments), encoding="utf-8")
    run_ffmpeg(["-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(output)])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reuse-audio", action="store_true")
    parser.add_argument("--output", default="sherlock_fin_ep01_google_tts.mp4")
    parser.add_argument("--tts", choices=["google", "cloud", "gemini", "sapi"], default="google")
    parser.add_argument("--cloud-language", default="ko-KR")
    parser.add_argument("--cloud-voice", default="ko-KR-Neural2-A")
    parser.add_argument("--gemini-model", default="gemini-2.5-flash-tts")
    parser.add_argument("--gemini-voice", default="Kore")
    parser.add_argument(
        "--gemini-prompt",
        default="따뜻하고 다정한 어린이 그림책 낭독가처럼, 천천히 또박또박 읽어 주세요. 페이지의 감정을 살리되 과장하지 말고 포근하게 읽어 주세요.",
    )
    parser.add_argument("--speaking-rate", type=float, default=0.9)
    parser.add_argument("--pitch", type=float, default=0.0)
    parser.add_argument("--page-gap", type=float, default=0.8)
    parser.add_argument("--list-cloud-voices", action="store_true")
    args = parser.parse_args()

    if args.list_cloud_voices:
        for voice in list_cloud_voices(args.cloud_language):
            name = voice.get("name", "")
            gender = voice.get("ssmlGender", "")
            sample_rate = voice.get("naturalSampleRateHertz", "")
            languages = ",".join(voice.get("languageCodes", []))
            print(f"{name}\t{gender}\t{sample_rate}\t{languages}")
        return 0

    pages = read_script()
    if not pages:
        raise RuntimeError("No TTS pages found.")

    segments = build_segments(
        pages,
        reuse_audio=args.reuse_audio,
        tts=args.tts,
        cloud_voice=args.cloud_voice,
        cloud_language=args.cloud_language,
        gemini_model=args.gemini_model,
        gemini_prompt=args.gemini_prompt,
        gemini_voice=args.gemini_voice,
        speaking_rate=args.speaking_rate,
        pitch=args.pitch,
        page_gap=args.page_gap,
    )
    output = OUT_DIR / args.output
    concatenate(segments, output)
    duration = sum(ffprobe_duration(segment) for segment in segments)
    print(f"Created: {output}")
    print(f"Duration: {math.ceil(duration)} seconds")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {html.escape(str(exc))}", file=sys.stderr)
        raise
