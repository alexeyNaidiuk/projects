import os

import unittest
from dotenv import load_dotenv

load_dotenv()


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        proxies_folder = os.environ.get('PROXIES_FOLDER')
        targets_folder = os.environ.get('TARGETS_FOLDER')
        key = os.environ.get('ZENNO_KEY')
        serv_host = os.environ.get('SERV_HOST')
        self.assertIsNot(proxies_folder, '')
        self.assertIsNot(targets_folder, '')
        self.assertIsNot(key, '')
        self.assertIsNot(serv_host, '')
