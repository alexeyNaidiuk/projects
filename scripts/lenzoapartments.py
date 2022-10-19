import requests
from faker import Faker

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        headers = {
            'authority': 'lenzoapartments.eu',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://lenzoapartments.eu',
            'referer': 'https://lenzoapartments.eu/en_GB/contact',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': Faker().chrome(),
        }
        post_data = {
            'namew': 'name',
            'emailw': target,
            'subjectw': 'Zmiana rezerwacji',
            'message': text,
            'scty': [
                '0',
                '1',
            ],
            'sub': 'Send',
        }
        response = requests.post('https://lenzoapartments.eu/en_GB/contact', headers=headers, data=post_data,
                                 proxies=proxies, verify=False)
        return response


if __name__ == '__main__':
    success_message = 'Thank You!'
    project_name = 'lenzoapartments'
    promo_link = 'bit.ly/3RyZp6f'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
