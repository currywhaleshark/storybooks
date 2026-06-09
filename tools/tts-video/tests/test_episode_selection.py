import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SERVER_PATH = REPO_ROOT / "tools" / "tts-video" / "server.py"
APP_PATH = REPO_ROOT / "tools" / "tts-video" / "public" / "app.js"


def load_server():
    spec = importlib.util.spec_from_file_location("tts_video_server", SERVER_PATH)
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

    def test_frontend_does_not_force_popo_as_default_episode(self):
        app = APP_PATH.read_text(encoding="utf-8")

        self.assertNotIn('title.includes("포포는_안_졸려")', app)


if __name__ == "__main__":
    unittest.main()
