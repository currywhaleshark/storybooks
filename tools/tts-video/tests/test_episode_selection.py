import importlib.util
import subprocess
import unittest
from unittest import mock
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SERVER_PATH = REPO_ROOT / "tools" / "tts-video" / "server.py"
APP_PATH = REPO_ROOT / "tools" / "tts-video" / "public" / "app.js"
INDEX_PATH = REPO_ROOT / "tools" / "tts-video" / "public" / "index.html"
START_CMD_PATH = REPO_ROOT / "tools" / "tts-video" / "start_tts_video_server.cmd"
RENDERER_PATH = (
    REPO_ROOT
    / "series"
    / "sherlock-fin-deep-city"
    / "videos"
    / "누가_먼저_왔을까_tts_google"
    / "make_tts_video.py"
)


def load_server():
    spec = importlib.util.spec_from_file_location("tts_video_server", SERVER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_renderer():
    spec = importlib.util.spec_from_file_location("tts_video_renderer_test", RENDERER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class EpisodeSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = load_server()
        cls.series_root = REPO_ROOT / "series" / "coral-town-daycare"

    def script_names_for(self, episode_title):
        return [item["name"] for item in self.server.script_candidates(self.series_root, episode_title)]

    def test_script_candidates_do_not_mix_other_episode_scripts(self):
        names = self.script_names_for("포포는_안_졸려")

        self.assertIn("popo_naptime_story_prompts.md", names)
        self.assertNotIn("루루야_약속했잖아_tts.md", names)
        self.assertNotIn("루루야_약속했잖아.md", names)

    def test_matching_tts_script_is_preferred(self):
        names = self.script_names_for("루루야_약속했잖아")

        self.assertGreaterEqual(len(names), 2)
        self.assertEqual(names[0], "루루야_약속했잖아_tts.md")
        self.assertEqual(names[1], "루루야_약속했잖아.md")

    def test_juni_episode_prefers_matching_prompt_document(self):
        names = self.script_names_for("준이의_싫어싫어파도")

        self.assertEqual(names[0], "준이의_싫어싫어파도.md")
        self.assertNotIn("루루야_약속했잖아_tts.md", names)

    def test_frontend_does_not_force_popo_as_default_episode(self):
        app = APP_PATH.read_text(encoding="utf-8")

        self.assertNotIn('title.includes("포포는_안_졸려")', app)

    def test_loads_series_tts_voice_presets(self):
        preset = self.server.load_tts_voice_presets(self.series_root)

        self.assertEqual(preset["seriesId"], "coral-town-daycare")
        self.assertEqual(preset["defaultVoice"], "Kore")
        self.assertTrue(preset["sameVoicePolicy"])
        self.assertEqual(preset["characters"]["lulu"]["label"], "루루")
        self.assertEqual(preset["characters"]["lulu"]["voice"], "Kore")
        self.assertIn("[excitedly]", preset["characters"]["lulu"]["tagCandidates"])

    def test_extracts_saved_tts_script_markdown(self):
        script = self.server.build_script_markdown(
            "테스트_에피소드",
            ["series/test/images/episodes/sample/final/00_표지.png", "series/test/images/episodes/sample/final/01_페이지.png"],
            ["표지 문장입니다.", "[excitedly] 다시 불러온 원고입니다.\n\n두 번째 줄도 유지합니다."],
        )

        self.assertEqual(
            self.server.extract_text_blocks(script),
            ["표지 문장입니다.", "[excitedly] 다시 불러온 원고입니다.\n\n두 번째 줄도 유지합니다."],
        )

    def test_extracts_korean_text_blocks_from_prompt_document(self):
        path = self.series_root / "docs" / "episodes" / "준이의_싫어싫어파도.md"
        texts = self.server.extract_text_blocks(path.read_text(encoding="utf-8"))

        self.assertEqual(len(texts), 11)
        self.assertIn("준이의 싫어싫어파도", texts[0])
        self.assertIn("아침이 되었어요.", texts[1])
        self.assertIn("준이 마음도", texts[-1])

    def test_extracts_all_unfenced_page_text_blocks_without_shifting_dialogue_page(self):
        path = (
            REPO_ROOT
            / "series"
            / "sherlock-fin-deep-city"
            / "docs"
            / "episodes"
            / "밤에_빛나는_길.md"
        )

        texts = self.server.extract_text_blocks(path.read_text(encoding="utf-8"))

        self.assertEqual(len(texts), 12)
        self.assertEqual(texts[0], "심해탐정 셜록 핀\n\n밤에 빛나는 길")
        self.assertIn("딥시티에\n포근한 밤이 왔어요.", texts[1])
        self.assertTrue(texts[9].startswith("“안녕하세요!”"))
        self.assertTrue(texts[9].endswith("나는 통 몰랐지 뭐냐.”"))
        self.assertIn("꼬마 탐정단,\n오늘도 성공!", texts[11])

    def test_extracts_plain_text_blocks_with_document_level_outer_quotes(self):
        markdown = '''### 00 표지

Text:
"표지 문장"

### 01

Text:
"첫 페이지 문장."
'''

        self.assertEqual(self.server.extract_text_blocks(markdown), ["표지 문장", "첫 페이지 문장."])

    def test_preserves_empty_plain_text_pages_without_shifting_later_pages(self):
        markdown = '''### 00 표지

Text:
표지 문장

### 01

Text:

### 02

Text:
마지막 문장
'''

        self.assertEqual(self.server.extract_text_blocks(markdown), ["표지 문장", "", "마지막 문장"])

    def test_frontend_fetches_tts_presets_and_inserts_audio_tags(self):
        app = APP_PATH.read_text(encoding="utf-8")

        self.assertIn("/api/tts-presets", app)
        self.assertIn("insertAudioTag", app)
        self.assertIn("presetCharacterSelect", app)

    def test_frontend_reuses_directly_selected_script_on_extract(self):
        app = APP_PATH.read_text(encoding="utf-8")

        self.assertIn("directScriptContent", app)
        self.assertIn("if (state.directScriptContent)", app)
        self.assertIn('scriptSelect.addEventListener("change"', app)

    def test_frontend_reports_extracted_count_before_padding_empty_editors(self):
        app = APP_PATH.read_text(encoding="utf-8")

        self.assertEqual(app.count("const extractedCount = state.texts.length;"), 2)
        self.assertEqual(app.count("state.selected.imageCount - extractedCount"), 2)

    def test_frontend_shows_korean_tooltips_for_audio_tags(self):
        app = APP_PATH.read_text(encoding="utf-8")

        self.assertIn("const TAG_TRANSLATIONS", app)
        self.assertIn('"[excitedly]": "신나게"', app)
        self.assertIn("function tagTooltipText", app)
        self.assertIn("button.title = tagTooltipText(tag);", app)
        self.assertIn('button.setAttribute("aria-label", tagTooltipText(tag));', app)

    def test_frontend_shows_broad_audio_tag_catalog_with_translations(self):
        app = APP_PATH.read_text(encoding="utf-8")
        html = INDEX_PATH.read_text(encoding="utf-8")

        self.assertIn('id="audioTagCatalog"', html)
        self.assertIn("const AUDIO_TAG_CATALOG", app)
        self.assertIn("function renderAudioTagCatalog", app)
        self.assertIn("function tagButtonLabel", app)
        self.assertIn('"감정"', app)
        self.assertIn('"속도와 쉼"', app)
        self.assertIn('"소리와 반응"', app)
        self.assertIn('"[excitedly]", "신나게"', app)
        self.assertIn('"[whispers]", "속삭이며"', app)
        self.assertIn('"[short pause]", "짧게 쉬기"', app)
        self.assertIn('button.textContent = tagButtonLabel(tag);', app)
        self.assertIn("insertAudioTag(tag)", app)

    def test_renderer_bypasses_disabled_local_proxy_for_https_calls(self):
        renderer = load_renderer()

        self.assertTrue(hasattr(renderer, "open_url"))
        self.assertTrue(hasattr(renderer, "direct_url_opener"))

        HTTPSHandler = type("HTTPSHandler", (), {})

        class DummyOpener:
            handlers = [HTTPSHandler()]

            def open(self, request, timeout):
                return {"url": request.full_url, "timeout": timeout}

        with mock.patch.dict(renderer.os.environ, {"HTTPS_PROXY": "http://127.0.0.1:9"}, clear=True):
            with mock.patch.object(renderer, "direct_url_opener", return_value=DummyOpener()):
                with mock.patch.object(renderer, "urlopen", side_effect=AssertionError("normal urlopen used")):
                    result = renderer.open_url(renderer.Request("https://oauth2.googleapis.com/token"), timeout=7)

        self.assertEqual(result, {"url": "https://oauth2.googleapis.com/token", "timeout": 7})

    def test_renderer_falls_back_to_curl_when_https_handler_is_missing(self):
        renderer = load_renderer()

        class DummyOpener:
            handlers = []

            def open(self, request, timeout):
                raise AssertionError("urllib opener should not be used without HTTPSHandler")

        completed = subprocess.CompletedProcess(args=[], returncode=0, stdout=b'{"ok": true}', stderr=b"")
        request = renderer.Request(
            "https://example.test/token",
            data=b"grant_type=refresh_token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )

        with mock.patch.dict(renderer.os.environ, {"HTTPS_PROXY": "http://127.0.0.1:9"}, clear=True):
            with mock.patch.object(renderer, "direct_url_opener", return_value=DummyOpener()):
                with mock.patch.object(renderer.subprocess, "run", return_value=completed) as run:
                    response = renderer.open_url(request, timeout=9)

        self.assertEqual(response.read(), b'{"ok": true}')
        args = run.call_args.args[0]
        self.assertIn("curl.exe", args[0])
        self.assertIn("--noproxy", args)
        self.assertIn("*", args)
        self.assertIn("https://example.test/token", args)

    def test_renderer_audio_uses_isolated_subprocess_for_gemini_tts(self):
        completed = subprocess.CompletedProcess(args=[], returncode=0, stdout="ok", stderr="")

        with mock.patch.object(self.server.subprocess, "run", return_value=completed) as run:
            with mock.patch.object(self.server.RENDERER, "download_cloud_tts", side_effect=AssertionError("in-process TTS used")):
                self.server.renderer_audio(
                    {
                        "tts": "gemini",
                        "geminiVoice": "Kore",
                        "geminiModel": "gemini-3.1-flash-tts-preview",
                        "geminiPrompt": "따뜻하게",
                        "speakingRate": 0.95,
                        "pitch": 0.1,
                    },
                    "짧은 테스트입니다.",
                    REPO_ROOT / "tools" / "tts-video" / "runtime" / "test.mp3",
                )

        args = [str(arg) for arg in run.call_args.args[0]]
        self.assertIn(str(RENDERER_PATH), args)
        self.assertIn("--sample-text", args)
        self.assertIn("짧은 테스트입니다.", args)
        self.assertIn("--sample-output", args)
        self.assertIn("--gemini-model", args)
        self.assertIn("gemini-3.1-flash-tts-preview", args)
        python_dir = Path(self.server.renderer_python_executable()).resolve().parent
        env_path = run.call_args.kwargs["env"]["PATH"].split(";")
        self.assertEqual(env_path[0], str(python_dir))
        self.assertEqual(env_path[1], str(python_dir / "DLLs"))
        self.assertNotIn("PYTHONHOME", run.call_args.kwargs["env"])

    def test_cloud_voice_list_uses_isolated_subprocess(self):
        completed = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout="ko-KR-Chirp3-HD-Kore\tFEMALE\t24000\tko-KR\n",
            stderr="",
        )

        with mock.patch.object(self.server.subprocess, "run", return_value=completed) as run:
            with mock.patch.object(self.server.RENDERER, "list_cloud_voices", side_effect=AssertionError("in-process voice list used")):
                voices = self.server.renderer_cloud_voices("ko-KR")

        args = [str(arg) for arg in run.call_args.args[0]]
        self.assertIn("--list-cloud-voices", args)
        self.assertIn("--cloud-language", args)
        python_dir = Path(self.server.renderer_python_executable()).resolve().parent
        env_path = run.call_args.kwargs["env"]["PATH"].split(";")
        self.assertEqual(env_path[0], str(python_dir))
        self.assertEqual(env_path[1], str(python_dir / "DLLs"))
        self.assertNotIn("PYTHONHOME", run.call_args.kwargs["env"])
        self.assertEqual(voices[0]["name"], "ko-KR-Chirp3-HD-Kore")
        self.assertEqual(voices[0]["gender"], "FEMALE")

    def test_windows_start_script_runs_server_with_cloud_sdk_python(self):
        self.assertTrue(START_CMD_PATH.exists(), "Windows start script should exist")
        script = START_CMD_PATH.read_text(encoding="utf-8")

        self.assertIn("Google\\Cloud SDK\\google-cloud-sdk\\platform\\bundledpython\\python.exe", script)
        self.assertIn("-X utf8", script)
        self.assertIn("server.py", script)
        self.assertIn("cd /d", script)


if __name__ == "__main__":
    unittest.main()
