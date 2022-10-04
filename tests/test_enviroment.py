import os

import unittest
from dotenv import load_dotenv

load_dotenv()


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        print()
        proxies_folder = os.environ.get('PROXIES_FOLDER')
        targets_folder = os.environ.get('TARGETS_FOLDER')
        self.assertIsNot(proxies_folder, '')
        self.assertIsNot(targets_folder, '')
