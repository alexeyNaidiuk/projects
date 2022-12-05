import unittest

from module.config import ZENNO_KEY, SERV_HOST, CAPMONSTER_HOST


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        self.assertIsNotNone(ZENNO_KEY)
        self.assertIsNotNone(SERV_HOST)
        # self.assertIsNotNone(CAPMONSTER_HOST)
