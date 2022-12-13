import requests

import module

INDEX_PHP = 'https://steinmetz-nuss.de/index.php'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://steinmetz-nuss.de',
    'Referer': 'https://steinmetz-nuss.de/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'nameInput': self.get_text(),
            'mailInput': target,
            'messageInput': self.get_text(),
            'copyInput': 'on',
            'submit': 'Send',
        }

        response = requests.post(INDEX_PHP, headers=headers, data=data, proxies=self.get_proxies(), timeout=5)
        return response


if __name__ == '__main__':
    project_name = 'steinmetz'
    s = 'Ihre Nachricht wurde erfolgreich gesendet.'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3BUJXMX'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
