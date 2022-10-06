import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text: str, target: str, proxies: dict) -> requests.Response:
        cookies = {
            '_ga': 'GA1.2.979444820.1664892536',
            '_gid': 'GA1.2.1945924821.1664892536',
            '__gads': 'ID=f853e126c27ba4dc-227fddcb3ace002f:T=1664892514:RT=1664892514:S=ALNI_MYaz_E0z5KnwNcKltGfBJMvmTbqGA',
            '__gpi': 'UID=00000b5c036f199a:T=1664892514:RT=1664892514:S=ALNI_MZsutwb2WC6zFX2v0KTb6Ar7OfyNw',
        }
        headers = {
            'authority': 'tlxgroup.biz',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'origin': 'https://tlxgroup.biz',
            'referer': 'https://tlxgroup.biz/contact-us',
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
        content = {
            'contact_name': text,
            'contact_email': target,
            'contact_message': text,
            'contact_copy': '1',
        }
        response = requests.post('https://tlxgroup.biz/contact-us', cookies=cookies, headers=headers, data=content,
                                 proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'successfully'
    project_name = 'tlxgroup'
    promo_link = 'bit.ly/3e5xE7u'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    result = spam.send_post()  # True no email
    # if result:
    #     spam.run_concurrently()
