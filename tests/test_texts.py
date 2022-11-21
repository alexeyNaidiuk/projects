import unittest

from module.texts import Text


class TestText(unittest.TestCase):

    def test_get_text_with_stickers(self):
        promo_link = 'google.com'
        text_language = 'ru'
        with_stickers = True
        text = Text(promo_link, text_language)
        result = text.get_text(with_stickers=with_stickers)
        self.assertIn(promo_link, result)

        self.assertIn('🔥', result)
        self.assertIn('👉', result)
        self.assertIn('👈', result)

    def test_get_text_without_stickers(self):
        promo_link = 'google.com'
        text_language = 'ru'
        with_stickers = False
        text = Text(promo_link, text_language)
        result = text.get_text(with_stickers=with_stickers)
        self.assertIn(promo_link, result)

        self.assertNotIn('🔥', result)
        self.assertNotIn('👉', result)
        self.assertNotIn('👈', result)
