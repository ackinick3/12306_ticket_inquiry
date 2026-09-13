import json
import tempfile
import unittest
from pathlib import Path

from config_loader import load_headers


class LoadHeadersTests(unittest.TestCase):
    def test_loads_cookie_and_user_agent_as_request_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            config_path = Path(directory) / "config.json"
            config_path.write_text(
                json.dumps({"cookie": "cookie-value", "user_agent": "agent-value"}),
                encoding="utf-8",
            )

            self.assertEqual(
                load_headers(config_path),
                {"Cookie": "cookie-value", "User-Agent": "agent-value"},
            )

    def test_rejects_a_config_missing_required_private_values(self):
        with tempfile.TemporaryDirectory() as directory:
            config_path = Path(directory) / "config.json"
            config_path.write_text(json.dumps({"cookie": "cookie-value"}), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "user_agent"):
                load_headers(config_path)


if __name__ == "__main__":
    unittest.main()
