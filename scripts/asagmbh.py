import requests

import module

url = 'https://www.asa-gmbh-bln.de/'
DATA = '------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="frm_action"\r\n\r\ncreate\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="form_id"\r\n\r\n2\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="frm_hide_fields_2"\r\n\r\n\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="form_key"\r\n\r\nom-contact-form\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[0]"\r\n\r\n\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="frm_submit_entry_2"\r\n\r\nedafc77bc5\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="_wp_http_referer"\r\n\r\n/\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="frm_verify"\r\n\r\n\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[6]"\r\n\r\nFrau\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[15]"\r\n\r\ntest\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[7]"\r\n\r\ntest https://www.testasa-gmbh-bln.de/#kontakt\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[8]"\r\n\r\ntest\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[9]"\r\n\r\n2112121212\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[10]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[11]"\r\n\r\ntest\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_meta[12][]"\r\n\r\nIch bin mit der Übertragung und Speicherung meiner persönlichen Daten zur Abwicklung des E-Mail- oder Telefonverkehrs einverstanden. Von den mir zustehenden Rechten im Bereich <a target="_blank" href="/datenschutz/">Datenschutz</a> habe ich Kenntnis genommen. Mit dem Absenden dieses Formulars akzeptiere ich die Speicherung meiner Daten.\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh\r\nContent-Disposition: form-data; name="item_key"\r\n\r\n\r\n------WebKitFormBoundary0j7NnEM43AzAvvKh--\r\n'
headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0j7NnEM43AzAvvKh',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(url, headers=headers, data=data.encode())
        return response


if __name__ == '__main__':
    project_name = 'asagmbh'
    s = 'Ihre Mitteilung wurde erfolgreich übermittelt. Vielen Dank!'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3WoPRxu'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
