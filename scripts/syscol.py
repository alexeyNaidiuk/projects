import requests

from module.spam_abstraction import Spam

url = 'https://syscol.com/site/contact.aspx'
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://syscol.com',
    'Referer': 'https://syscol.com/contacto.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        data = {
            'Nombre': text,
            'Email': target,
            # 'To': 'softumwork@gmail.com',
            'Teléfono 1': 'test',
            'Teléfono 2': 'test',
            'Colegio': 'test',
            'Motivo': 'info-mas',
            'Mensaje': 'test',
            'Hash': '@28391127132022931414',
        }

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'OK'
    project_name = 'syscol'
    promo_link = 'bit.ly/3USvtE3'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
