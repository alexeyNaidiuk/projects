import requests

import module

url = 'https://hxuevil4.paperform.co/api/v1/form/5f7c65ec1d47c23a5635a8b5/submit'

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
                    'value': 'test https://workroutes.co.uk/sign-up-page/',
                },
                {
                    'key': 'a90bi',
                    'value': '12212121222',
                },
                {
                    'key': 'gtqe',
                    'value': target,
                },
                {
                    'key': 'bu23o',
                    'value': 'test https://workroutes.co.uk/sign-up-page/',
                },
                {
                    'key': '699oa',
                    'value': 'No',
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clb3iy4ug00002v6ufqy6o9ig',
            'deviceId': 'clb3iy4ug00012v6udoclfkn1',
        }

        response = requests.post(url, headers=headers, json=json_data,
                                 # proxies=self.get_proxies(),
                                 timeout=10)
        return response


if __name__ == '__main__':
    project_name = 'hxuevil4'
    success_message = '"errors":null'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3iSH0FF'
    spam = ConcreteSpam(
        project_name, success_message, referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
