import requests

import module

url = 'https://workersrights.com/me-plus-three/'
headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarymUTAoMpNidrlUD0F',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_4.3"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_5"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_8.3"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_10"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_9.3"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="input_11"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJbXSIsIjgxYWUzZTY0NmE4YjFiY2UyMWZlZjI2ZWZjNDVmMTM2Il0=\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundarymUTAoMpNidrlUD0F--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text()).encode()

        response = requests.post(url,
                                 headers=headers,
                                 data=data,
                                 # timeout=10,
                                 # proxies=self.get_proxies()
                                 )
        return response


if __name__ == '__main__':
    project_name = 'workersrights'
    s = 'Thank You'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3Y5H05u'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
