import requests

from module.spam_abstraction import Spam

cookies = {
    'humans_21909': '1',
}

headers = {
    'authority': 'hhisolutions.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'humans_21909=1',
    'origin': 'https://hhisolutions.com',
    'referer': 'https://hhisolutions.com/contact-us/',
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

    def post(self, target) -> requests.Response:


        data = {
            'contact_name': target,
            'contact_email': target,
            'contact_subject': self.get_text(),
            'contact_message': 'Получи 50 free spins за Регистрацию в клубе по ссылке ниже https://bit.ly/3NXJdev Торопись, время действия приза ограничено!',
            'contact_email_copy': '1',
            'submit': '1',
        }

        response = requests.post('https://hhisolutions.com/contact-us/', cookies=cookies, headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you!'
    project_name = 'hhisolutions'
    promo_link = 'bit.ly/3NXJdev'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently(5)