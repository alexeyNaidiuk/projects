import requests

from module.spam_abstraction import Spam

headers = {
    'cookie': 'YII_CSRF_TOKEN=05dabdb18038be7f10d781ef05caa65c5ef1fa04s%3A40%3A%22b4618c95af1e587bb3a18e9bff8841d86d96f9a6%22%3B',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryXunuIXwwScRpdlbb',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="YII_CSRF_TOKEN"\r\n\r\nb4618c95af1e587bb3a18e9bff8841d86d96f9a6\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[name]"\r\n\r\ntest https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[phone]"\r\n\r\ntest https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[comment]"\r\n\r\ntest https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[ch1]"\r\n\r\n0\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[ch1]"\r\n\r\n1\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="TxA76CSd@qYtU8kWgSFzEx4ePUyb2d5F"\r\n\r\n\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb--\r\n'

url = 'https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku',
                            self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)
        response = requests.post(url, proxies=self.get_proxies(), headers=headers, data=data, verify=False)
        return response


if __name__ == '__main__':
    success_message = 'Спасибо'
    project_name = '7sbgfx1atah4a'
    promo_link = 'bit.ly/3GKAZVL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
