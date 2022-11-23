import requests

from module.spam_abstraction import Spam

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryXWsWlY9DozM2bHO5',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n3419\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_cust_image"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n3649\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n1\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\n\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_captcha_res"\r\n\r\n59\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5\r\nContent-Disposition: form-data; name="wp_iec_captcha_ans"\r\n\r\n17131f29aa095b5e1087814f05cacd71ce1f29b7\r\n------WebKitFormBoundaryXWsWlY9DozM2bHO5--\r\n'

url = 'https://bounceandplaytwo.ca/invitation/'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(url, headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank you'
    project_name = 'bounceandplaytwo'
    promo_link = 'bit.ly/3GOHLtg'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
