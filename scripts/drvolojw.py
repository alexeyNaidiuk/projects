import requests

import module

url = 'https://yyefqkhj.paperform.co/api/v1/form/608be2ebef9d880f44129961/submit'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
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

        response = requests.post(url, headers=headers, json=json_data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'drvolojw'
    s = '"errors":null'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3gE7zxX'
    spam = ConcreteSpam(project_name, s, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
