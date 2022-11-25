import requests

from module.spam_abstraction import Spam

url = 'https://www.sspsap-motherhouse.nl/publications/e-cards/christmas/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOqWQIRzddHdMPBKK',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n2728\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n3303\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text())
        data = data.replace('softumwork@gmail.com', target)
        response = requests.post(url, headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'THANK YOU'
    project_name = 'sspsap'
    promo_link = 'bit.ly/3UZNYGL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
