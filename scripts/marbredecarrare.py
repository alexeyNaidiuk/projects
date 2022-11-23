import requests

from module.spam_abstraction import Spam

url = 'https://marbredecarrare.fr/wp-admin/admin-ajax.php'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryG53vywoObbD7FXYF',
}

data = '------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="contact-name"\r\n\r\ntest\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="contact-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="contact-message"\r\n\r\ntest\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="contact-sendcopy"\r\n\r\n1\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="gdpr"\r\n\r\n1\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="action"\r\n\r\nbuilder_contact_send\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n3310\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="orig_id"\r\n\r\n1330\r\n------WebKitFormBoundaryG53vywoObbD7FXYF\r\nContent-Disposition: form-data; name="element_id"\r\n\r\n32ri603\r\n------WebKitFormBoundaryG53vywoObbD7FXYF--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        post_data = data.replace('softumwork@gmail.com', target)
        post_data = post_data.replace('test', self.get_text())

        response = requests.post(url, headers=headers, data=post_data.encode())
        return response


if __name__ == '__main__':
    success_message = 'Thank you.'
    project_name = 'marbredecarrare'
    promo_link = 'bit.ly/3CEv81r'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
