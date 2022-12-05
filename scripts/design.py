import requests

import module

url = 'http://functional-design.de/price-list.html'

headers = {
    'Cookie': 'csrf_contao_csrf_token=337jQocl593ldOrBwu3SArpwElAmcYbERwjaGBI7wq4',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'FORM_SUBMIT': 'auto_form_63',
            'REQUEST_TOKEN': '337jQocl593ldOrBwu3SArpwElAmcYbERwjaGBI7wq4',
            'name': text,
            'fon': target,
            'email': target,
            'strasse': target,
            'plz': target,
            'stadt': target,
            'lieferstrasse': target,
            'lieferstadt': target,
            'message': target,
            'bestellung_spoiler': target,
            'cc': [
                '',
                'cc',
            ],
            'captcha_851': '9',
            'captcha_851_hash': 'f3e04eed26285536ada896368170a52b13c048d018f5d85d019d6c5993ba31c7',
            'captcha_851_name': '',
        }

        response = requests.post(
            url, headers=headers, data=data, verify=False,
            proxies=self.get_proxies()
        )
        return response


if __name__ == '__main__':
    project_name = 'design'
    s = 'Thank you for your email!'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3iyJzwC'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
