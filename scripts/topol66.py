import requests

from module.spam_abstraction import Spam

url = 'https://topol66.ru/secoh'

cookies = {
    'PHPSESSID': 'fd0d08421d3dc1ae7e1b20e52e0d8fad',
    'YII_CSRF_TOKEN': '670abc384e1eda75b70c3a9c1ac1034444ded2das%3A40%3A%22056437125fd9e4ea1730ee681a955f322e924cd5%22%3B',
}

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryAk7VPmg7i0BnxQ8h',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

data = '------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="YII_CSRF_TOKEN"\r\n\r\n056437125fd9e4ea1730ee681a955f322e924cd5\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="addr"\r\n\r\ntopol66.ru/secoh\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="name"\r\n\r\n\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[fio]"\r\n\r\ntest\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[phone]"\r\n\r\ntest\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[message]"\r\n\r\ntest\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[attachment]"\r\n\r\n\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[attachment]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[copy]"\r\n\r\n0\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="OrderForm[copy]"\r\n\r\n1\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="dX5syd7TfB67j#ZcBHBNnh2nP4jTAvBA"\r\n\r\n\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h\r\nContent-Disposition: form-data; name="yt0"\r\n\r\nОтправить\r\n------WebKitFormBoundaryAk7VPmg7i0BnxQ8h--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        post_data = data.replace('softumwork@gmail.com', target)
        post_data = post_data.replace('test', self.get_text())

        response = requests.post(url, cookies=cookies, headers=headers, data=post_data.encode(),
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'разблокирована'
    project_name = 'topol66'
    promo_link = 'bit.ly/3i84g21'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
