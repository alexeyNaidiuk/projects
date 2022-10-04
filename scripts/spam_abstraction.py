import logging

import requests
from requests_toolbelt import MultipartEncoder

from module import data


class ConcreteSpam(data.Spam):

    def post(self, text, target, proxies) -> requests.Response:
        ...


if __name__ == '__main__':
    spam = ConcreteSpam('bit.ly/3Sm168r', 'solutions2share', success_message='thank-you-for-your-message',
                        logging_level=logging.INFO, text_encoding='utf-8')
    result = spam.send_post()
    if result:
        data.func_concurrently(spam.main, 50)
