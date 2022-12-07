import requests

import module

url = 'https://reflex.rocks/e-cards/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryrWhI6dfRDICIE6ap',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n15331\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n15361\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\n\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryrWhI6dfRDICIE6ap--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(url, headers=headers, data=data,
                                 proxies=self.get_proxies(),
                                 timeout=5)
        return response


if __name__ == '__main__':
    project_name = 'reflex'
    s = 'Thanks for your support!'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VZkI3k'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
