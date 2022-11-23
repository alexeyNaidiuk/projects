import requests

from module.spam_abstraction import Spam

url = 'http://www.tfevrazia.ru/bronirovanie_ekskursii'

headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarypgdgFW52QX3z8Qip',
    'Cookie': 'PHPSESSID=ac97ebb4cd8c5b844faa007ff9ead97f',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[fos_no]"\r\n\r\n29\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[attrib][pole30][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[attrib][pole31][pole]"\r\n\r\n+79659659659\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[attrib][pole53][pole]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[attrib][pole32][pole]"\r\n\r\n"Приглашаем в мир кино"\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[attrib][pole50][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[attrib][pole117][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[send_me]"\r\n\r\n0\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="FosUnlimForm[send_me]"\r\n\r\n1\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip\r\nContent-Disposition: form-data; name="EmH4j9-d6-M3tCcSYUVPG--Ck_jFpTWb"\r\n\r\n\r\n------WebKitFormBoundarypgdgFW52QX3z8Qip--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text())

        response = requests.post(url, headers=headers, data=data.encode(), verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Спасибо!'
    project_name = 'tfevrazia'
    promo_link = 'bit.ly/3VnaI3C'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
