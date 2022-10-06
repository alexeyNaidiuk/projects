import unittest

from module import TurkeyTargetServerPool, ServerPool


class TestRetrieveFromServer(unittest.TestCase):

    def test_get_target(self):
        target_pool: ServerPool = TurkeyTargetServerPool()
        target = target_pool.pop()
        self.assertTrue('@' in target)
