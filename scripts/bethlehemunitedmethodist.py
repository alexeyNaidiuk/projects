import faker
import requests

import module

URL = 'https://bethlehemunitedmethodist.org/angel-ecards/'
DATA = '------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n12677\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n10102\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryjEEgU6B9Ha1z0OA6--\r\n'
cookies = {
    '_gid': 'GA1.2.1246832577.1671012150',
    '_clck': '131bbsn|1|f7e|0',
    '_ga': 'GA1.2.1498445390.1670505199',
    '_gat_gtag_UA_99765856_1': '1',
    '_clsk': 'cl59yj|1671012213439|2|1|m.clarity.ms/collect',
    '_ga_3LE381DK8P': 'GS1.1.1671012150.2.1.1671012248.0.0.0',
    '_gali': 'wp-iec-submit-btn-10102',
}
headers = {
    'authority': 'bethlehemunitedmethodist.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryjEEgU6B9Ha1z0OA6',
    # 'cookie': '_gid=GA1.2.1246832577.1671012150; _clck=131bbsn|1|f7e|0; _ga=GA1.2.1498445390.1670505199; _gat_gtag_UA_99765856_1=1; _clsk=cl59yj|1671012213439|2|1|m.clarity.ms/collect; _ga_3LE381DK8P=GS1.1.1671012150.2.1.1671012248.0.0.0; _gali=wp-iec-submit-btn-10102',
    'origin': 'https://bethlehemunitedmethodist.org',
    'referer': 'https://bethlehemunitedmethodist.org/angel-ecards/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        headers['user-agent'] = faker.Faker().chrome()
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(
            URL, cookies=cookies, headers=headers, data=data.encode(),
            proxies=self.get_proxies(),
            timeout=10
        )
        return response


if __name__ == '__main__':
    project_name = 'bethlehemunitedmethodist'
    s = 'Your Angel ecard was sent successfully.'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FRvTWP'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
