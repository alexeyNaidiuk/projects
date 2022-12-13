import unittest

from module.texts import Text


class TestText(unittest.TestCase):

    def test_get_text_with_stickers(self):
        promo_link = 'google.com'
        text_language = 'ru'
        project = 'fortuneclock'
        spins = '50'

        text = Text(lang=text_language, link=promo_link, project=project)

        result = text.get_text(with_stickers=True)
        print(result)
        self.assertIn(promo_link, result)
        self.assertIn(project.capitalize(), result)
        self.assertIn(spins, result)
        self.assertIn('🔥', result)
        self.assertIn('👉', result)
        self.assertIn('👈', result)

        result = text.get_text(with_stickers=False)
        print(result)
        self.assertNotIn('🔥', result)
        self.assertNotIn('👉', result)
        self.assertNotIn('👈', result)

    def test_link_encoding(self):
        reference = 'https%3A%2F%2Fbit.ly%2F3BUJXMX'
        link = 'bit.ly/3BUJXMX'
        project = 'fortuneclock'

        text = Text(lang='ru', link=link, project=project)

        result = text.get_text()
        print(result)
