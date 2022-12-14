import requests

import module

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylHnEn3UvismmNwNO',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
cookies = {
}
URL = 'https://marbredecarrare.fr/wp-admin/admin-ajax.php'
DATA = '------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="contact-name"\r\n\r\ntest\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="contact-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="contact-message"\r\n\r\ntest\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="contact-sendcopy"\r\n\r\n1\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="gdpr"\r\n\r\n1\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="action"\r\n\r\nbuilder_contact_send\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n166\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="orig_id"\r\n\r\n166\r\n------WebKitFormBoundarylHnEn3UvismmNwNO\r\nContent-Disposition: form-data; name="element_id"\r\n\r\nuu6h178\r\n------WebKitFormBoundarylHnEn3UvismmNwNO--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text()).encode()
        response = requests.post(URL, cookies=cookies, headers=headers, data=data)
        return response


if __name__ == '__main__':
    project_name = 'marbredecarrare'
    s = 'Thank you.'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3huErcz'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
