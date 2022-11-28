import requests

from unittest import TestCase

from module.link_shortner import LinkShortner


class TestLinkShortner(TestCase):

    def test_get_link(self):

        url = 'https://referencemen.live/ktVmDV?c=0097xLek_pT9MBb54378f54e94879e&utm_campaign=mixru'
        shortened_link = LinkShortner.get_link(url)
        self.assertIn('bit.ly', shortened_link)
        response = requests.get('https://%s' % shortened_link)
        response_content = response.text
        self.assertIn('slottica', response_content)
