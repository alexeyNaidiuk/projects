import requests

from module.spam_abstraction import Spam

import requests

cookies = {
    'PHPSESSID': 'ddb73503150c38f599ad6d13c1ce1ced',
}

headers = {
    'authority': 'xn--80aaf4abkmbdych.xn--p1ai',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary6esDHvh7GLEzZB3b',
    # 'cookie': 'PHPSESSID=ddb73503150c38f599ad6d13c1ce1ced',
    'origin': 'https://xn--80aaf4abkmbdych.xn--p1ai',
    'referer': 'https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

url = 'https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:

        data = '------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="Advert[name]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[username]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[phone]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="Advert[description]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[images][]"\r\n\r\n\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[images][]"\r\n\r\n\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="tgdhYSf_mV3J3phTV4yMCnpzsUf@rMS2"\r\n\r\n\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="copyForMe"\r\n\r\n1\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="yt0"\r\n\r\nПодать объявление\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text(False))

        response = requests.post(url, cookies=cookies,
                                 headers=headers, data=data.encode().decode('latin-1'), proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Ваше объявление было успешно отправлено.'
    project_name = 'p1ai'
    promo_link = 'bit.ly/3tFtur4'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently()
