import requests

import module

url = 'https://nf77-widerruf.paperform.co/api/v1/form/6318548d9dabce494509355c/submit'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        json_data = {
            'data': [
                {
                    'key': '9tdn8',
                    'value': 'Ja',
                },
                {
                    'key': 'flkft',
                    'value': 'Ja',
                },
                {
                    'key': 'f96jk',
                    'value': self.get_text(),
                },
                {
                    'key': '3bn7e',
                    'value': target,
                },
                {
                    'key': '9a230',
                    'value': 'test',
                },
                {
                    'key': 'epdij',
                    'value': 'Einzelne Artikel',
                },
                {
                    'key': '8avks',
                    'value': 'test',
                },
                {
                    'key': 'aa8r3',
                    'value': 'Ja',
                },
                {
                    'key': 'rdp9',
                    'value': 'https://s3.amazonaws.com/pf-user-files-01/u-231300/uploads/2022-11-30/yt22usq/yt12u9i.png',
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clb3llpzl00002v6uuvl3t6bt',
            'deviceId': 'clb3lh9k900012v6utah3ljo8',
        }
        response = requests.post(url, headers=headers, json=json_data, proxies=self.get_proxies(), timeout=10)
        return response


if __name__ == '__main__':
    project_name = 'widerruf'
    success_message = '"errors":null'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3ioqo8P'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
