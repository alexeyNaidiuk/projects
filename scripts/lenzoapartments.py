import logging

import requests
from faker import Faker

from module import data


class ConcreteSpam(data.Spam):

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
            'namew': 'test',
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
                                 proxies=proxies)
        return response


if __name__ == '__main__':
    spam = ConcreteSpam('bit.ly/3RyZp6f', 'lenzoapartments', success_message='Thank You!',
                        logging_level=logging.INFO, text_encoding='utf-8')
    result = spam.send_post()
    spam.run_concurrently()
