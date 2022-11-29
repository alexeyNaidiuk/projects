import requests

import module

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://drvolojw.paperform.co/api/v1/form/61b0b2302b1f2a6d506de00f/submit'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        json_data = {
            'data': [
                {
                    'key': 'f2t63',
                    'value': self.get_text(),
                },
                {
                    'key': 'ah0u2',
                    'value': target,
                },
                {
                    'key': 'ajgvn',
                    'value': self.get_text(),
                },
                {
                    'key': '3nmcu',
                    'value': '21212121',
                },
                {
                    'key': '75mo7',
                    'value': target,
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clb23fxgd00002v6u3t2n3yph',
            'deviceId': 'clb22y7in00012v6usjhckzm2',
        }
        response = requests.post(url, headers=headers, json=json_data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'drvolojw'
    s = '"errors":null'

    spam = ConcreteSpam(project_name, s)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
