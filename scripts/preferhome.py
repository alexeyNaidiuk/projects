import faker
import requests

import module

url = 'https://preferhome.com/email-form/'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'user-agent': faker.Faker().chrome(),
        }

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
            data=data,
            proxies=self.get_proxies(),
            timeout=10
        )
        return response


if __name__ == '__main__':
    project_name = 'preferhome'
    s = 'Thank you'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FioVID'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
