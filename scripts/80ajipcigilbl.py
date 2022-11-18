import requests

from module.spam_abstraction import Spam

url = 'http://www.xn--80ajipcigilbl.xn--p1ai/kontaktyi'

cookies = {
    'PHPSESSID': '61fb561e07c96b53b4b7af0347d66b6c',
    '_ym_uid': '1668784531382201553',
    '_ym_d': '1668784531',
    '_ym_isad': '2',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://www.xn--80ajipcigilbl.xn--p1ai',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.xn--80ajipcigilbl.xn--p1ai/kontaktyi',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'QuestForm[name]': self.get_text(),
            'QuestForm[phone]': '+7956598645',
            'QuestForm[email]': target,
            'QuestForm[comment]': target,
            'QuestForm[send_me]': [
                '0',
                '1',
            ],
            'N#9Uy3MVXNP#g6tcyFewyygUnjH8s5D': '',
            'yt0': '',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Спасибо'
    project_name = '80ajipcigilbl'
    promo_link = 'bit.ly/3EjO3hR'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
