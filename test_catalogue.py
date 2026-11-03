# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
from main import create_app
from downloader import fetch_items, write_snapshot


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "movies.json"
        self.client = create_app(self.path).test_client()

    def test_missing_data(self):
        self.assertEqual(self.client.get("/").status_code, 503)

    def test_html_is_escaped(self):
        write_snapshot(self.path, [{"title": "<script>alert(1)</script>", "synopsis": "<img src=x onerror=alert(1)>"}])
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"<script>alert(1)</script>", response.data)
        self.assertIn(b"&lt;script&gt;", response.data)

    def test_snapshot_replacement(self):
        write_snapshot(self.path, [{"title": "first"}])
        write_snapshot(self.path, [{"title": "second"}])
        response = self.client.get("/")
        self.assertIn(b"second", response.data)
        self.assertNotIn(b"<strong>first</strong>", response.data)
        self.assertEqual(len(list(self.path.parent.iterdir())), 1)

    def test_missing_key_never_requests(self):
        with patch("downloader.requests.get") as get:
            with self.assertRaises(ValueError):
                fetch_items("")
            get.assert_not_called()

    def test_mocked_api_validation(self):
        response = Mock()
        response.json.return_value = {"ITEMS": [{"title": "example"}]}
        with patch("downloader.requests.get", return_value=response) as get:
            self.assertEqual(fetch_items("test")[0]["title"], "example")
            self.assertEqual(get.call_args.kwargs["timeout"], 15)
        response.json.return_value = {"ITEMS": ["bad"]}
        with patch("downloader.requests.get", return_value=response):
            with self.assertRaises(ValueError):
                fetch_items("test")


if __name__ == "__main__":
    unittest.main()
