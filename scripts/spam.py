import requests

from module.data import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        ...


if __name__ == '__main__':
    success_message = ''
    project_name = 'test'
    promo_link = 'bit.ly/3RxKclL'
    spam = ConcreteSpam(promo_link, project_name, success_message, logging_level='debug')
    result = spam.send_post()
    # if result:
    #     spam.run_concurrently()
