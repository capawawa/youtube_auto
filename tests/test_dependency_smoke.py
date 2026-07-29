import importlib
import os
import unittest
from unittest import mock


class DependencySmokeTests(unittest.TestCase):
    @mock.patch.dict(
        os.environ,
        {"OPENAI_API_KEY": "dependency-smoke-placeholder"},
        clear=False,
    )
    def test_application_module_imports(self):
        module = importlib.import_module("main")

        self.assertTrue(callable(module.create_video))

    def test_runtime_imports(self):
        import aiohttp  # noqa: F401
        import google_auth_httplib2  # noqa: F401
        import mutagen  # noqa: F401
        import pydub  # noqa: F401
        import tkinter  # noqa: F401
        from dotenv import load_dotenv  # noqa: F401
        from google_auth_oauthlib.flow import InstalledAppFlow  # noqa: F401
        from googleapiclient.discovery import build  # noqa: F401
        from gtts import gTTS  # noqa: F401
        from PIL import Image  # noqa: F401

    def test_moviepy_v1_api_used_by_application(self):
        import numpy as np
        from moviepy.editor import ImageClip

        clip = ImageClip(np.zeros((2, 2, 3), dtype=np.uint8)).set_duration(1)
        try:
            self.assertEqual(clip.duration, 1)
        finally:
            clip.close()

    def test_openai_client_api_used_by_application(self):
        from openai import Client

        client = Client(api_key="dependency-smoke-placeholder")
        try:
            self.assertIsNotNone(client.chat.completions)
        finally:
            client.close()


if __name__ == "__main__":
    unittest.main()
