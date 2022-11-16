import unittest

from module.spam_abstraction import Spam


class TestSpamInterface(unittest.TestCase):

    def test_interface_init_method(self):
        promo_link = 'bit.ly/3hwcEby'
        success_message = ''
        project_name = 'test_case'
        spam = Spam(promo_link, project_name, success_message)
        # todo check type of fields
        #   Pool, Text, ProjectController

    def test_get_text(self):
        promo_link = 'bit.ly/3hwcEby'
        success_message = ''
        project_name = 'test_case'
        text_lang = 'ru'
        spam = Spam(promo_link, project_name, success_message, text_lang=text_lang)
        result = spam.get_text()
        text_lang = 'tr'
        spam = Spam(promo_link, project_name, success_message, text_lang=text_lang)
        result = spam.get_text()
        text_lang = 'eng'
        spam = Spam(promo_link, project_name, success_message, text_lang=text_lang)
        result = spam.get_text()

    def test_get_proxies(self):
        promo_link = 'bit.ly/3hwcEby'
        success_message = ''
        project_name = 'test_case'
        proxy_pool = 'west'
        spam = Spam(promo_link, project_name, success_message, proxy_pool=proxy_pool)
        spam.get_proxies()
        proxy_pool = 'wwmix'
        spam = Spam(promo_link, project_name, success_message, proxy_pool=proxy_pool)
        spam.get_proxies()
        proxy_pool = 'checked'
        spam = Spam(promo_link, project_name, success_message, proxy_pool=proxy_pool)
        spam.get_proxies()
