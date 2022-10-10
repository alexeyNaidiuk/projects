import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '8a25a0a0c56f512c2a9838eb31e1ce6f': '40d80d3174d3bbef1b4dbfc17a9365c3',
            '_ym_uid': '16648910031008422294',
            '_ym_d': '1664891003',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
        }
        headers = {
            'authority': 'www.oes.cat',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.oes.cat',
            'referer': 'https://www.oes.cat/index.php/contact-us',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        post_data = {
            'name': text,
            'email': target,
            'message': text,
            'subject': text,
            'date': '06/10/2022',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '112',
        }
        response = requests.post('https://www.oes.cat/index.php/contact-us', cookies=cookies, headers=headers,
                                 data=post_data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'oes'
    promo_link = 'bit.ly/3CwaWPp'
    spam = ConcreteSpam(promo_link, project_name, success_message=success_message)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently(10)
