import os
import unittest

from module import TurkeyTargetFilePool, TARGETS_FOLDER


class TestTurkeyTargetPool(unittest.TestCase):
    def setUp(self) -> None:
        self.pool = TurkeyTargetFilePool()

    def test_pool_is_not_empty(self):
        self.assertTrue(len(self.pool) != 0)

    def test_pool_updates(self):
        for _ in range(len(self.pool)):
            self.pool.pop()
        self.pool.pop()
        self.assertNotEqual(len(self.pool), 0)
