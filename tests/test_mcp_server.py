import json
import unittest
from pathlib import Path
import mcp_server


class TestMCPServer(unittest.TestCase):
    def test_list_tracks(self):
        res = mcp_server.list_tracks()
        self.assertIn("Music For Robots", res)
        self.assertIn("cathartic-callbacks", res)

    def test_get_track(self):
        res = mcp_server.get_track("cathartic-callbacks")
        data = json.loads(res)
        self.assertEqual(data.get("track", {}).get("slug"), "cathartic-callbacks")
        self.assertIn("reviews", data)

    def test_get_analysis(self):
        res = mcp_server.get_analysis("cathartic-callbacks")
        data = json.loads(res)
        self.assertIn("spectral", data.get("analysis", {}))
        self.assertIn("dynamics", data.get("analysis", {}))

    def test_search_reviews(self):
        res = mcp_server.search_reviews("amplitude")
        self.assertIn("segment(s) matching 'amplitude'", res)

    def test_get_aligned_segments_full(self):
        res = mcp_server.get_aligned_segments("cathartic-callbacks")
        data = json.loads(res)
        self.assertEqual(data["track"]["slug"], "cathartic-callbacks")
        self.assertGreater(data["segment_counts"]["total_in_window"], 0)
        self.assertIn("timeline", data)
        self.assertIn("acoustic_baseline", data)

    def test_get_aligned_segments_window(self):
        res = mcp_server.get_aligned_segments("cathartic-callbacks", start_sec=5.0, end_sec=15.0)
        data = json.loads(res)
        self.assertEqual(data["query_window"]["start_sec"], 5.0)
        self.assertEqual(data["query_window"]["end_sec"], 15.0)
        for seg in data["timeline"]:
            self.assertLessEqual(seg["time_sec"], 15.0)
            self.assertGreaterEqual(seg["end_time_sec"], 5.0)

    def test_get_aligned_segments_invalid_window(self):
        res = mcp_server.get_aligned_segments("cathartic-callbacks", start_sec=20.0, end_sec=10.0)
        self.assertIn("Invalid time window", res)

    def test_get_aligned_segments_invalid_slug(self):
        res = mcp_server.get_aligned_segments("non-existent-slug")
        self.assertIn("not found", res)

    def test_get_critic_contrast(self):
        res = mcp_server.get_critic_contrast("cathartic-callbacks")
        data = json.loads(res)
        self.assertEqual(data["track"]["slug"], "cathartic-callbacks")
        self.assertIn("vincent", data["critic_profiles"])
        self.assertIn("robach", data["critic_profiles"])
        self.assertIn("critic_tension_index", data["contrast_metrics"])
        self.assertIn("regularization_vector", data["contrast_metrics"])

    def test_get_critic_contrast_single_critic_track(self):
        res = mcp_server.get_critic_contrast("chasing-leaks-climax")
        data = json.loads(res)
        self.assertEqual(data["track"]["slug"], "chasing-leaks-climax")
        self.assertIn("critic_tension_index", data["contrast_metrics"])

    def test_get_sections(self):
        res = mcp_server.get_sections("cathartic-callbacks")
        self.assertTrue("section(s)" in res or "has no sections" in res)

    def test_list_sections(self):
        res = mcp_server.list_sections()
        self.assertIsInstance(res, str)

    def test_get_dequantization_skill(self):
        res = mcp_server.get_dequantization_skill("music-for-robots")
        self.assertIn("music-for-robots", res)


if __name__ == "__main__":
    unittest.main()
