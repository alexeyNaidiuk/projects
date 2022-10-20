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

    def test_files(self):
        targets_folder = os.path.exists(TARGETS_FOLDER)
        self.assertTrue(targets_folder)
        self.assertTrue(TARGETS_FOLDER + '/all_turk.csv')
        proxies_folder = os.path.exists(PROXIES_FOLDER)
        self.assertTrue(proxies_folder)
        self.assertTrue(PROXIES_FOLDER + '/wwmix.txt')
