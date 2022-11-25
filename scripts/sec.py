import requests

from module.spam_abstraction import Spam

headers = {
    'authority': 'sec-e.co.za',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://sec-e.co.za',
    'referer': 'https://sec-e.co.za/index.php/ar/contact-us',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-csrf-token': 'b3eb2df24ad944fcfaf22a9e36f3e00e',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://sec-e.co.za/index.php/ar/contact-us'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:

        data = {
            'name': 'name',
            'email': target,
            'message': self.get_text(),
            'subject': '🔥 50 free spins за регистрацию! 🔥',
            'date': '30/11/2022',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '112',
        }

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = '{"status":1,"message":"Your email has been sent."}'
    project_name = 'sec'
    promo_link = 'bit.ly/3F2xo46'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
