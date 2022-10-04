import unittest

from module import data


class TestRetrieveFromServer(unittest.TestCase):

    def test_get_target(self):
        server_controller = data.RetrieveFromServer()
        target = server_controller.get_target()
        print(target)
        self.assertIsNotNone(target)

    def test_append_target(self):
        server_controller = data.RetrieveFromServer()
        server_controller.append_target('softumwork@gmail.com')
