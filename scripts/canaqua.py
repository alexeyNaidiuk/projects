import faker
import requests

import module

URL = 'https://canaqua.ca/wp-json/contact-form-7/v1/contact-forms/3782/feedback'

DATA = '------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n3782\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.4\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f3782-p2040-o1\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n2040\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="your-friend-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundarykkv5wh0rnGZRNTff--\r\n'
cookies = {
    'PHPSESSID': '95dde8a0baad777ba29e415fea519b89',
}

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarykkv5wh0rnGZRNTff',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers['user-agent'] = faker.Faker().chrome()

        data = DATA.replace('softumwork@gmail.com', target)
        data = data.replace('test', self.get_text(False))
        response = requests.post(
            URL,
            cookies=cookies,
            headers=headers,
            data=data.encode(),
            proxies=self.get_proxies(),
            timeout=10
        )
        return response


if __name__ == '__main__':
    project_name = 'canaqua'
    s = 'It has been sent.'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3hwlzdf'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
