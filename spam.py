import requests

from module.spam_abstraction import Spam


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        ...


if __name__ == '__main__':
    success_message = ''
    project_name = 'spam'
    promo_link = 'bit.ly/3CEv81r'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
