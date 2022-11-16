import requests

from module.spam_abstraction import Spam

cookies = {
    '_ga': 'GA1.2.1316780931.1668604650',
    '_gid': 'GA1.2.747382109.1668604650',
    '_gat': '1',
}

headers = {
    'authority': 'www.sspsap-motherhouse.nl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOqWQIRzddHdMPBKK',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.1316780931.1668604650; _gid=GA1.2.747382109.1668604650; _gat=1',
    'origin': 'https://www.sspsap-motherhouse.nl',
    'referer': 'https://www.sspsap-motherhouse.nl/publications/e-cards/christmas/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n2728\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n3303\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryOqWQIRzddHdMPBKK--\r\n'
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)
        response = requests.post('https://www.sspsap-motherhouse.nl/publications/e-cards/christmas/', cookies=cookies,
                                 headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'THANK YOU'
    project_name = 'sspsap'
    promo_link = 'bit.ly/3UZNYGL'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
