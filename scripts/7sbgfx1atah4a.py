import requests

from module.spam_abstraction import Spam

cookies = {
    'PHPSESSID': '0060696de3d6e101e8db4d35b0902dee',
    'YII_CSRF_TOKEN': '05dabdb18038be7f10d781ef05caa65c5ef1fa04s%3A40%3A%22b4618c95af1e587bb3a18e9bff8841d86d96f9a6%22%3B',
    '_ga': 'GA1.2.294710793.1669197664',
    '_gid': 'GA1.2.1698109495.1669197664',
    '_ym_uid': '1669197665776165832',
    '_ym_d': '1669197665',
    '_ym_visorc': 'w',
    'tmr_lvid': '69834594bbd6f26c5ec6d1f17de23b6c',
    'tmr_lvidTS': '1669197666477',
    '_ym_isad': '2',
    'hunter_start': '%7B%22s%22%3A1669197670384%7D',
    '_gat': '1',
    'tmr_detect': '0%7C1669198137645',
    'tmr_reqNum': '14',
}

headers = {
    'authority': 'xn----7sbgfx1atah4a.xn--p1ai',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryXunuIXwwScRpdlbb',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=0060696de3d6e101e8db4d35b0902dee; YII_CSRF_TOKEN=05dabdb18038be7f10d781ef05caa65c5ef1fa04s%3A40%3A%22b4618c95af1e587bb3a18e9bff8841d86d96f9a6%22%3B; _ga=GA1.2.294710793.1669197664; _gid=GA1.2.1698109495.1669197664; _ym_uid=1669197665776165832; _ym_d=1669197665; _ym_visorc=w; tmr_lvid=69834594bbd6f26c5ec6d1f17de23b6c; tmr_lvidTS=1669197666477; _ym_isad=2; hunter_start=%7B%22s%22%3A1669197670384%7D; _gat=1; tmr_detect=0%7C1669198137645; tmr_reqNum=14',
    'origin': 'https://xn----7sbgfx1atah4a.xn--p1ai',
    'referer': 'https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku',
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
DATA = '------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="YII_CSRF_TOKEN"\r\n\r\nb4618c95af1e587bb3a18e9bff8841d86d96f9a6\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[name]"\r\n\r\ntest https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[phone]"\r\n\r\ntest https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[comment]"\r\n\r\ntest https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[ch1]"\r\n\r\n0\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="FeedbackForm[ch1]"\r\n\r\n1\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb\r\nContent-Disposition: form-data; name="TxA76CSd@qYtU8kWgSFzEx4ePUyb2d5F"\r\n\r\n\r\n------WebKitFormBoundaryXunuIXwwScRpdlbb--\r\n'

url = 'https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test https://xn----7sbgfx1atah4a.xn--p1ai/otpravit_zayavku',
                            self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com',  target)
        response = requests.post(url, proxies=self.get_proxies(),
                                 cookies=cookies, headers=headers, data=data, verify=False)
        return response


if __name__ == '__main__':
    success_message = 'Спасибо'
    project_name = '7sbgfx1atah4a'
    promo_link = 'bit.ly/3GKAZVL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
