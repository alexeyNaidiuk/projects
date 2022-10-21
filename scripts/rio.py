import requests

from module import Spam

cookies = {
    'd2666dddef8ced0aa886295474275ac5': 'f8cc051abcb8a9ba85f60fb627f1f604',
    'df2603b7659f1473e79e16f80d24be52': 'en-GB',
}
headers = {
    'authority': 'rio.org.me',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'd2666dddef8ced0aa886295474275ac5=f8cc051abcb8a9ba85f60fb627f1f604; df2603b7659f1473e79e16f80d24be52=en-GB',
    'origin': 'https://rio.org.me',
    'referer': 'https://rio.org.me/index.php/en/contact',
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
data = {
    'jform[contact_name]': 'test',
    'jform[contact_email]': 'softumwork@gmail.com',
    'jform[contact_subject]': 'test',
    'jform[contact_message]': 'test',
    'jform[contact_email_copy]': '1',
    'option': 'com_contact',
    'task': 'contact.submit',
    'return': '',
    'id': '1:contact-name',
    'd65f1da75e1d30863f5920cd5080f90d': '1',
}
url = 'https://rio.org.me/index.php/en/contact'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data['jform[contact_email]'] = target
        data['jform[contact_name]'] = text
        data['jform[contact_subject]'] = text
        data['jform[contact_message]'] = text

        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for contacting us'
    project_name = 'rio'
    promo_link = 'bit.ly/3yV4jUL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(5)
