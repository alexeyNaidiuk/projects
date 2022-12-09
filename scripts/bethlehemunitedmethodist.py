import requests
from faker import Faker

import module

url = 'https://bethlehemunitedmethodist.org/angel-ecards/'

DATA = '------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n12689\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n10102\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarylvgy46BgLoaXdpkS--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylvgy46BgLoaXdpkS',
            'user-agent': Faker().chrome(),
        }
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(url,
                                 headers=headers,
                                 data=data.encode(),
                                 # proxies=self.get_proxies(),
                                 # timeout=10
                                 )
        return response


if __name__ == '__main__':
    project_name = 'bethlehemunitedmethodist'
    s = 'successfully'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FFeyQP'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
