import requests

import module

url = 'https://www.fluxlogistix.com/wp-json/contact-form-7/v1/contact-forms/370/feedback'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7uErlJplwvPXA7RS',
}

DATA = '------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n370\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.3\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_GB\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f370-p2240-o1\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n2240\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary7uErlJplwvPXA7RS\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundary7uErlJplwvPXA7RS--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(
            url,
            headers=headers,
            data=data.encode(),
        )
        return response


if __name__ == '__main__':
    project_name = 'fluxlogistix'
    s = 'has been sent.'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3W1byn2'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
