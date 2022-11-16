import requests

from module.spam_abstraction import Spam

url = 'https://kifa.dp.ua/kontakty'

cookies = {
    'f38a4dc02eaf72fddb10b6e4a01f791e': '1c05489fdce53d8013f0ce5313050f95',
}

headers = {
    'authority': 'kifa.dp.ua',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'f38a4dc02eaf72fddb10b6e4a01f791e=1c05489fdce53d8013f0ce5313050f95',
    'origin': 'https://kifa.dp.ua',
    'referer': 'https://kifa.dp.ua/kontakty',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        data = {
            'vcontact_name': text,
            'vcontact_email': target,
            'vcontact_subject': text,
            'vcontact_message': target,
            'vcontact_copy': 'on',
            'vtbutton': 'Send Message',
            'user_id': '0',
            'ip': '194.183.168.2',
            'title': 'Контакты, телефоны, карта | компания "Кифа", лестницы в г.Днепр',
            'referrer': 'https://kifa.dp.ua/kontakty',
            'mid': 'vcontact_id107',
            'f80f0949552762df3fb9194646a90939': '1',
        }

        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your contact.'
    project_name = 'kifa'
    promo_link = 'bit.ly/3X7iFeV'
    spam = ConcreteSpam(promo_link, project_name, success_message, proxy_pool='wwmix')
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
