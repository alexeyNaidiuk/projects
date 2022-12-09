import requests

import module

url = 'https://www.ihugs.cloud/birthdays/'
headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryvqocLKGUC2BK9kwr',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        DATA = '------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n277\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n132\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest https://www.ihugs.cloud/birthdays/\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest https://www.ihugs.cloud/birthdays/\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\n\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest https://www.ihugs.cloud/birthdays/\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_schedule"\r\n\r\n\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryvqocLKGUC2BK9kwr--\r\n'
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(url, headers=headers, data=data,
                                 # proxies=self.get_proxies(),
                                 # timeout=10
                                 )
        return response


if __name__ == '__main__':
    project_name = 'ihugs'
    s = 'Thank You'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3W1lfBY'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
