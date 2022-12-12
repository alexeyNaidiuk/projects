import requests
from faker import Faker

import module

url = 'https://www.sotecnisol.pt/'

params = {
    'fp': '9200',
    'f_id': '30',
    'responseType': 'json',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'User-Agent': Faker().chrome(),
        }

        data = {
            'iziFormDefinedField_name': self.get_text(False),
            'iziFormDefinedField_email': target,
        }

        response = requests.post(url, params=params, headers=headers, data=data, proxies=self.get_proxies())
        print(response.text)
        return response


if __name__ == '__main__':
    project_name = 'sotecnisol'
    s = 'Parabéns, registou-se com sucesso na nossa newsletter.'

    project = 'luckybird'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FLv4Pk'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
