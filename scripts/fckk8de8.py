import requests

import module

uurl = 'https://fckk8de8.paperform.co/api/v1/form/5d5dad6cf76b5c09800fed45/submit'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        json_data = {
            'data': [
                {
                    'key': '9n9er',
                    'value': self.get_text(),
                },
                {
                    'key': 'e6ace',
                    'value': self.get_text(),
                },
                {
                    'key': 'm28h',
                    'value': target,
                },
                {
                    'key': '6735d',
                    'value': '1221212112',
                },
                {
                    'key': 'f1ht8',
                    'value': self.get_text(),
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clb3lu7is00002v6u4jts2nn3',
            'deviceId': 'clb3llefs00012v6uq7ajtatd',
        }
        response = requests.post(uurl, headers=headers, json=json_data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'fckk8de8'
    success_message = '"errors":null'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VigrIA'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
