import requests

from module.spam_abstraction import Spam

url = 'https://workersrights.com/me-plus-three/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryCj1CmkB9HeoczPXR',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
data = '------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_1.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_1.6"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_2"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_4.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_5"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_8.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_10"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_9.3"\r\n\r\ntest https://workersrights.com/me-plus-three/\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="input_11"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="is_submit_1"\r\n\r\n1\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_submit"\r\n\r\n1\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_unique_id"\r\n\r\n\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="state_1"\r\n\r\nWyJbXSIsIjgxYWUzZTY0NmE4YjFiY2UyMWZlZjI2ZWZjNDVmMTM2Il0=\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_target_page_number_1"\r\n\r\n0\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_source_page_number_1"\r\n\r\n1\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR\r\nContent-Disposition: form-data; name="gform_field_values"\r\n\r\n\r\n------WebKitFormBoundaryCj1CmkB9HeoczPXR--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        post_data = data.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(url, headers=headers, data=post_data.encode(),
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'THANK YOU'
    project_name = 'workersrights'
    promo_link = 'bit.ly/3AQL7bo'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
