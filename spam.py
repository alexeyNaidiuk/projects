import requests

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        ...


if __name__ == '__main__':
    project_name = 'spam'
    success_message = ''

    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
