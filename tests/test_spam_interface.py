import unittest

from module.spam_abstraction import Spam


class TestSpamInterface(unittest.TestCase):

    def test_interface_init_method(self):
        promo_link = 'bit.ly/3hwcEby'
        success_message = 'empty'
        project_name = 'test_case'
        spam = Spam(promo_link, project_name, success_message)
