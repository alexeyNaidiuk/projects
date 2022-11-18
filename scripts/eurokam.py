import requests

from module.spam_abstraction import Spam

url = 'http://www.eurokam-ural.ru/ostavit_soobschenie'

cookies = {
    'PHPSESSID': 'a731f9cd9a7213a768d6432ebec3d858',
    '_ym_uid': '1668789982480303509',
    '_ym_d': '1668789982',
    '_ym_isad': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryrIMr0waXJ7fZ0Xmz',
    'Origin': 'http://www.eurokam-ural.ru',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.eurokam-ural.ru/ostavit_soobschenie',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[fos_no]"\r\n\r\n1\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[attrib][pole2][pole]"\r\n\r\ntest\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[attrib][pole3][pole]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[attrib][pole4][pole]"\r\n\r\ntest\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[attrib][pole6][pole]"\r\n\r\ntest\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[send_me]"\r\n\r\n0\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="FosForm[send_me]"\r\n\r\n1\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz\r\nContent-Disposition: form-data; name="kVQMdpjsvrvKRWzNb4r5h9SQpZG3pgtG"\r\n\r\n\r\n------WebKitFormBoundaryrIMr0waXJ7fZ0Xmz--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text().encode().decode('latin-1'))

        response = requests.post(url, cookies=cookies, headers=headers, data=data, verify=False,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Спасибо за обращение!'
    project_name = 'eurokam'
    promo_link = 'bit.ly/3EKP3gz'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
