import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        ...


if __name__ == '__main__':
    success_message = ''
    project_name = 'test'
    promo_link = 'bit.ly/3RxKclL'
    spam = ConcreteSpam(promo_link, project_name, success_message, logging_level='debug')
    res = spam.send_post()
    if res:
        spam.run_concurrently()
