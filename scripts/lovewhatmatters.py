import requests

import module

url = 'https://lovewhatmatters.paperform.co/api/v1/form/5f07790ec4b7be528e794c46/submit'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        json_data = {
            'data': [
                {
                    'key': '2fmc7',
                    'value': self.get_text(),
                },
                {
                    'key': 'aq1n5',
                    'value': 'Yes',
                },
                {
                    'key': '621a4',
                    'value': target,
                },
                {
                    'key': '2eumv',
                    'value': '2132121',
                },
                {
                    'key': '3n8aj',
                },
                {
                    'key': 'f67g6',
                    'value': self.get_text(),
                },
                {
                    'key': 'auh5k',
                    'value': 'https://s3.amazonaws.com/pf-user-files-01/u-68909/uploads/2022-12-05/fq12tvh/fq02tvb.png',
                },
                {
                    'key': 'ebu84',
                    'value': 'ACCEPT',
                },
                {
                    'key': '1rh3u',
                    'value': 'Yes',
                },
                {
                    'key': 'odrq',
                    'value': 'Yes',
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clbam4edk00002v6tdlltuves',
            'deviceId': 'clbam4edl00012v6tu91wtwv5',
        }
        response = requests.post(
            url,
            headers=headers,
            json=json_data,
            proxies=self.get_proxies(),
            timeout=5
        )
        return response


if __name__ == '__main__':
    project_name = 'lovewhatmatters'
    success_message = '"errors":null'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3P4RuOy'
    spam = ConcreteSpam(
        project_name, success_message,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
