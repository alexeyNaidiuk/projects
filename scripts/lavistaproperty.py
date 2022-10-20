import requests

from module import Spam

cookies = {
    'b8b2c462a5900427f0bf1ee84cabd574': 'f527848f3dbd5febcee65f943875952f',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.lavistaproperty.net',
    'Referer': 'http://www.lavistaproperty.net/index.php/contact-us2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = {
            'name': text,
            'email': target,
            'message': text,
            'subject': '121212',
            'date': '2022/11/12 13:08',
            'send_copy': '1',
            'task': 'sendmail',
            'ctajax_modid': '144',
        }

        response = requests.post('http://www.lavistaproperty.net/index.php/contact-us2', cookies=cookies,
                                 headers=headers, data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Your email has been sent.'
    project_name = 'lavistaproperty'
    promo_link = 'bit.ly/3gl2D0b'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
