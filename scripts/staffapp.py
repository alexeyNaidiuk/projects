import requests

import module

url = 'https://staffapp.paperform.co/api/v1/form/5f7b324e9fc00879d941ea26/submit'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        json_data = {
            'data': [
                {
                    'key': '2tdfs',
                    'value': self.get_text(),
                },
                {
                    'key': 'qfkr',
                    'value': self.get_text(),
                },
                {
                    'key': 'dmm8i',
                    'value': self.get_text(),
                },
                {
                    'key': '2mfh7',
                    'value': target,
                },
                {
                    'key': '2orvf',
                    'value': 'Eden Village Camp (Putnam Valley, NY)',
                },
                {
                    'key': 'elkpq',
                    'value': '',
                },
                {
                    'key': 'ab8ss',
                    'value': 'Yes!',
                },
                {
                    'key': '1rs5v',
                },
                {
                    'key': 'akhsc',
                    'value': [],
                },
                {
                    'key': 'b3h9l',
                },
                {
                    'key': 'bgck2',
                    'value': [],
                },
                {
                    'key': 'qepv',
                },
                {
                    'key': '2g3i4',
                },
                {
                    'key': 'eumnc',
                },
                {
                    'key': '2chp7',
                    'value': 'He/Him/His',
                },
                {
                    'key': 'd2opn',
                    'value': "Yes, I'm in high school",
                },
                {
                    'key': 'dc9l3',
                },
                {
                    'key': 'fs65j',
                    'value': self.get_text(),
                },
                {
                    'key': 'avsca',
                    'value': [
                        'Bunk Counselor',
                    ],
                },
                {
                    'key': 'csoi7',
                    'value': self.get_text(),
                },
                {
                    'key': 'e4492',
                    'value': [
                        'Lifeguarding',
                    ],
                },
                {
                    'key': '2fv11',
                },
                {
                    'key': '7vi9v',
                    'value': 'Yes',
                },
                {
                    'key': 'e5rkh',
                },
                {
                    'key': '9fuet',
                },
                {
                    'key': '4hup',
                    'value': [],
                },
                {
                    'key': 'fbo6s',
                    'value': [],
                },
                {
                    'key': '6uct',
                    'value': [],
                },
                {
                    'key': 'f2mis',
                    'value': [],
                },
                {
                    'key': 'fmmk7',
                },
                {
                    'key': 'ffkuv',
                },
                {
                    'key': '6i91g',
                    'value': [],
                },
                {
                    'key': '6n7p4',
                    'value': [
                        'CPR',
                    ],
                },
                {
                    'key': '83afe',
                },
                {
                    'key': 'ac6k5',
                },
                {
                    'key': '9nu99',
                },
                {
                    'key': '6mq00',
                },
                {
                    'key': '3h6hr',
                },
                {
                    'key': '6dsel',
                },
                {
                    'key': '4hbch',
                },
                {
                    'key': 'n7td',
                    'value': '',
                },
                {
                    'key': 'a7akb',
                },
                {
                    'key': '4o1b7',
                    'value': self.get_text(),
                },
                {
                    'key': '63dr0',
                    'value': self.get_text(),
                },
                {
                    'key': '28l8b',
                },
            ],
            'payment': None,
            'captcha': None,
            'score': False,
            'partialSubmissionId': 'clb3jlps600002v6u2eilpc3i',
            'deviceId': 'clb3jlps800012v6ufcc1tth9',
        }

        response = requests.post(url, headers=headers, json=json_data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'staffapp'
    success_message = '"errors":null'

    project = 'luckybird'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3XIG7iW'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
