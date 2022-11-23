import requests

from module.spam_abstraction import Spam

url = 'https://powdersvillepa.com/send-a-greeting/happy-birthday/'

headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryaAOdC8VAOVouTcy1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

data = '------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n8229\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n8250\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryaAOdC8VAOVouTcy1--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        post_data = data.replace('test', self.get_text()).replace('softumwork@gmail.com', target).encode()
        response = requests.post(url, headers=headers, data=post_data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'thankyou_redirect'
    project_name = 'powdersvillepa'
    promo_link = 'bit.ly/3VoPUJh'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
