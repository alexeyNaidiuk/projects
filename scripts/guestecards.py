import requests

from module.spam_abstraction import Spam

url = 'https://www.guestecards.com/ecard/waves-oceanfront-resort-email-postcards/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarywSqfBXdeKt8Kx9aM',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n257\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n254\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarywSqfBXdeKt8Kx9aM--\r\n'
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)

        response = requests.post(url, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'thankyou_redirect'
    project_name = 'guestecards'
    promo_link = 'bit.ly/3g8Nb7A'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post('worksoftum@gmail.com')
    if res:
        spam.run_concurrently()
