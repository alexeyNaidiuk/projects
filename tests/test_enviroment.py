import unittest

from module import KEY, SERV_HOST


class TestEnvironment(unittest.TestCase):

    def test_environment(self):
        self.assertIsNotNone(KEY)
        self.assertIsNotNone(SERV_HOST)
