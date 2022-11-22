import requests

from module.spam_abstraction import Spam

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarytZNK8mB0NvRgo00t',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

url = 'https://www.miniworldminiaturas.com.br/webforms/index/save/'
DATA = '------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="submitWebform_1"\r\n\r\n1\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="webform_id"\r\n\r\n1\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="referer_url"\r\n\r\nhttps://www.miniworldminiaturas.com.br/contato\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[1]"\r\n\r\ntest\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[2]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[4]"\r\n\r\ntest\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t\r\nContent-Disposition: form-data; name="field[3]"\r\n\r\ntest\r\n------WebKitFormBoundarytZNK8mB0NvRgo00t--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text(with_stickers=False).encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)
        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'sucesso'
    project_name = 'miniworldminiaturas'
    promo_link = 'bit.ly/3i235RS'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently()
