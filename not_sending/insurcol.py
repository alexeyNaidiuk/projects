import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '7bcf5425596cf7d1f30497618950f8d4': 't2h5uq485vr9bip40vdih5lf73',
            'c982ddb0a5f83a65456ea9f3f28d5cb0': 'es-ES',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://insurcol.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://insurcol.com/insurcol/index.php/es/pqr',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        data = {
            'jform[contact_name]': text,
            'jform[contact_email]': target,
            'jform[contact_subject]': text,
            'jform[contact_message]': text,
            'jform[contact_email_copy]': '1',
            'option': 'com_contact',
            'task': 'contact.submit',
            'return': '',
            'id': '8:datos-personales',
            '1d5edd0663cfc3b7d9838f201446a0c9': '1',
        }
        s = requests.Session()
        s.max_redirects = 60
        response = requests.post('http://insurcol.com/insurcol/index.php/es/pqr', cookies=cookies, headers=headers,
                                 data=data, proxies=proxies, allow_redirects=False, verify=False)
        return response


if __name__ == '__main__':
    success_message = ''
    project_name = 'insurcol'
    promo_link = 'bit.ly/3RLDlW2'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
