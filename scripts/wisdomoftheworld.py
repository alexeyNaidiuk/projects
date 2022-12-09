import requests

import module

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylsfZtEABELdUhlPi',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleW'
                  'ebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
url = 'https://www.wisdomoftheworld.com/offerings/wisdomcards/'
DATA = '------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n8392\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n7615\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarylsfZtEABELdUhlPi\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarylsfZtEABELdUhlPi--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(url, headers=headers, data=data.encode(), timeout=10)
        return response


if __name__ == '__main__':
    success_message = 'successfully'
    project_name = 'wisdomoftheworld'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3Y2KRQG'
    spam = ConcreteSpam(
        project_name, success_message, referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()  # True
    if res:
        spam.run_concurrently()
