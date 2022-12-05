import requests

import module

cookies = {
    '2a29f87150400d70daae53f386653885': '0r52ote0gr6lisl5rtj759s4k5uobre8',
    '_gcl_au': '1.1.181758461.1670242519',
    '_ga': 'GA1.2.1841839198.1670242521',
    '_gid': 'GA1.2.990670354.1670242521',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://www.jasper124massagetherapy.ca',
    'Referer': 'https://www.jasper124massagetherapy.ca/contact-us',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}
url = 'https://www.jasper124massagetherapy.ca/contact-us'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = {
            'formSent': '1',
            'jform[name]': 'name',
            'jform[email]': target,
            'jform[subject]': self.get_text(),
            'jform[message]': self.get_text(),
            'jform[sendcopy]': '1',
            'moduleId': '116',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'jasper124massagetherapy'
    success_message = 'Thank you'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3gYAaOn'
    spam = ConcreteSpam(
        project_name, success_message,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
