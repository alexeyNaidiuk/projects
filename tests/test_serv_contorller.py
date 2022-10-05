import unittest

from module import data


class TestRetrieveFromServer(unittest.TestCase):

    def test_get_target(self):
        server_controller = data.RetrieveFromServer()
        target = server_controller.get_target()
        self.assertIsNotNone(target)
