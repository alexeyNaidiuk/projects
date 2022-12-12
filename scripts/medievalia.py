import requests

import module

url = 'https://medievalia.com.ro/en/contact'
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

params = {
    'contact_ajax': '7130921670843909',
    'ctajax_modid': '105',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'name': self.get_text(),
            'email': target,
            'message': self.get_text(),
            'subject': self.get_text(),
            'send_copy': '1',
            'task': 'sendmail',
        }

        response = requests.post(url, params=params, headers=headers, data=data)
        return response


if __name__ == '__main__':
    project_name = 'medievalia'
    s = '{"status":1,"message":"Your email has been sent."}'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FkGYhE'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
