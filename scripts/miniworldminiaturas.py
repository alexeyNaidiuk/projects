import requests

from module.spam_abstraction import Spam

cookies = {
    'frontend': 'ac46mimc7r35gjviijurq52k76',
    'frontend_cid': '6fnw1vyowvHzlbm4',
    '_ga': 'GA1.4.368620688.1668775097',
    '_gid': 'GA1.4.1965769464.1668775097',
    '_pk_id.5.f9ee': '5ce2901ce6d8677d.1668775098.',
    '_pk_ses.5.f9ee': '1',
    '_gat': '1',
}

headers = {
    'authority': 'www.miniworldminiaturas.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarytZNK8mB0NvRgo00t',
    'origin': 'https://www.miniworldminiaturas.com.br',
    'referer': 'https://www.miniworldminiaturas.com.br/contato',
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

url = 'https://www.miniworldminiaturas.com.br/webforms/index/save/'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="submitWebform_1"\r\n\r\n1\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="webform_id"\r\n\r\n1\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="referer_url"\r\n\r\nhttps://www.miniworldminiaturas.com.br/contato\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[1]"\r\n\r\ntest\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[2]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[4]"\r\n\r\ntest\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[3]"\r\n\r\ntest\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t--\r\n'
        data = data.replace('test', self.get_text(with_stickers=False).encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)
        response = requests.post(url, cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'sucesso'
    project_name = 'miniworldminiaturas'
    promo_link = 'bit.ly/3V5Ju1p'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently()
