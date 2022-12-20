from unittest import TestCase

import requests

from module.link_shortner import LinkShortner


class TestLinkShortner(TestCase):

    def test_link(self):
        target_pool_name = 'mixru'
        referal_to_project = 'luckybird'

        shortened_link = LinkShortner.get_link(target_pool_name=target_pool_name, referal_to_project=referal_to_project)
        response = requests.get('https://%s' % shortened_link)
        response_content = response.text
        self.assertIn(referal_to_project, response_content)
