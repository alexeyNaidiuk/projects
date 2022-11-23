import requests

from module.spam_abstraction import Spam

url = 'http://gorod-dent.ru/personal/churkina_yuliya_mihaylovna'

headers = {
    'Cookie': 'PHPSESSID=93250d3f9da7dd57f4fbd7d41db101e2',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarytqI7Boil5Zqj75qW',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="FosLimitForm[fos_no]"\r\n\r\n56\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="FosLimitForm[attrib][pole57][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="FosLimitForm[attrib][pole59][pole]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="FosLimitForm[attrib][pole60][pole]"\r\n\r\ntest\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="zU__@cpMkEsrb_JMC-FqxGF2N@2KBQQ7"\r\n\r\n\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="FosLimitForm[send_me]"\r\n\r\n0\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW\r\nContent-Disposition: form-data; name="FosLimitForm[send_me]"\r\n\r\n1\r\n------WebKitFormBoundarytqI7Boil5Zqj75qW--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        response = requests.post(url, headers=headers, data=data, verify=False, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Ваш запрос принят к рассмотрению'
    project_name = 'gorod'
    promo_link = 'bit.ly/3U0DYMC'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
