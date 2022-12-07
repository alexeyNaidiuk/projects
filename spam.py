import requests

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        ...


if __name__ == '__main__':
    project_name = 'spam'
    s = ''

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VyF5El'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        # promo_link=promo_link
    )
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
