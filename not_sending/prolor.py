import requests

from module.spam_abstraction import Spam

url = 'http://prolor.net/index.php/information'


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        cookies = {
            'sj_hexagon_tpl': 'sj_hexagon',
            '7a6c57df3055f2c1bfe2403a515cb463': 'c4e1f5c77ad0d8065284a2cd608af0a3',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://prolor.net',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://prolor.net/index.php/information',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'contact_ajax': '9541511666012331',
            'ctajax_modid': '292',
        }

        data = {
            'name': 'test',
            'email': target,
            'message': "testreq",
            'subject': 'test',
            'send_copy': '1',
            'task': 'sendmail',
        }

        response = requests.post(url, params=params, cookies=cookies,
                                 headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'prolor'
    promo_link = 'bit.ly/3RrADoC'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()  # prolor bit.ly/3RrADoC 2022-10-20 10:57:09,960: True softumwork@gmail.com
    # if res:
    #     spam.run_concurrently()
