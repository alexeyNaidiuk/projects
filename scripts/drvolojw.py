import faker
import requests

import module

url = 'https://yyefqkhj.paperform.co/api/v1/form/608be2ebef9d880f44129961/submit'  # https://yesldn.org/refer/


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'user-agent': faker.Faker().chrome(),
        }
        json_data = {
            'data': [
                {
                    'key': '3pj7t',
                    'value': self.get_text(),
                },
                {
                    'key': 'etpf0',
                    'value': self.get_text(),
                },
                {
                    'key': 'a90bi',
                    'value': '12211221222',
                },
                {
                    'key': 'gtqe',
                    'value': target,
                },
                {
                    'key': 'bu23o',
                    'value': self.get_text(),
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clb3h409t00002v6u88bsju2z',
            'deviceId': 'clb3h3djy00012v6ur4l2q1wn',
        }

        response = requests.post(url, headers=headers, json=json_data,
                                 # proxies=self.get_proxies(),
                                 timeout=10)
        print(response.text)
        return response


if __name__ == '__main__':
    project_name = 'drvolojw'
    s = '"errors":null'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VMzCKP'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently(3)
