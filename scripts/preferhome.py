import requests

import module

url = 'https://preferhome.com/email-form/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'fm-name': self.get_text(),
            'fm-email': target,
            'fm-fname': self.get_text(),
            'fm-friend-email': target,
            'fm-comments': self.get_text(),
            'fm-previous-Title': '',
            'fm-previous-URL': 'preferhome.com',
            'Submit': 'Submit',
        }

        response = requests.post(
            url,
            headers=headers,
            data=data
        )
        return response


if __name__ == '__main__':
    project_name = 'preferhome'
    s = 'Thank you'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3P8sSV5'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
