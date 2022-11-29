import requests

from module.spam_abstraction import Spam

cookies = {
    '_ga': 'GA1.2.80408952.1668601763',
    '_gid': 'GA1.2.271451542.1668601763',
    '_pk_ref.25172.8302': '%5B%22%22%2C%22%22%2C1668601763%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.25172.8302': '1',
    '_fbp': 'fb.1.1668601763331.127951899',
    '_pk_id.25172.8302': '3ffc1fe2b3ba3164.1668601763.1.1668601859.1668601763.',
}
headers = {
    'authority': 'reflex.rocks',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarynFKTmBEq8AcOgBDK',
    'origin': 'https://reflex.rocks',
    'referer': 'https://reflex.rocks/e-cards/',
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
url = 'https://reflex.rocks/e-cards/'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n15331\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n15361\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_more_recipient"\r\n\r\n\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundarynFKTmBEq8AcOgBDK--\r\n'
        data = data.replace('test', self.get_text().encode().decode('latin-1'))
        data = data.replace('softumwork@gmail.com', target)
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thanks for your support!'
    project_name = 'reflex'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3u5uSUp'
    spam = ConcreteSpam(project_name, success_message, referal_project_name=project, promo_link=promo_link)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
