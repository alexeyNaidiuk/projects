import os

import unittest

from module import TARGETS_FOLDER, PROXIES_FOLDER


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        key = os.environ.get('ZENNO_KEY')
        serv_host = os.environ.get('SERV_HOST')
        self.assertIsNot(PROXIES_FOLDER, '')
        self.assertIsNot(TARGETS_FOLDER, '')
        self.assertIsNot(key, '')
        self.assertIsNot(serv_host, '')
