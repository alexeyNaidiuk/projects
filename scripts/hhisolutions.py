import requests

from module.spam_abstraction import Spam

headers = {
    'authority': 'hhisolutions.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'origin': 'https://hhisolutions.com',
    'referer': 'https://hhisolutions.com/contact-us/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
url = 'https://hhisolutions.com/contact-us/'


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:
        data = {
            'contact_name': text,
            'contact_email': target,
            'contact_subject': text,
            'contact_message': text,
            'contact_email_copy': '1',
            'submit': '1',
        }

        proxies = self.get_proxies()
        response = requests.post(url, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Your email was sent successfully. Thank you!'
    project_name = 'hhisolutions'
    promo_link = 'bit.ly/3NXJdev'
    spam = ConcreteSpam(promo_link, project_name, success_message, proxy_pool='checked')
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently(5)
