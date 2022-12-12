import requests

import module

url = 'https://vetcards.us/marines-family/'

headers = {
    'authority': 'vetcards.us',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryLDN4tcKfEzAYr03M',
    'origin': 'https://vetcards.us',
    'referer': 'https://vetcards.us/marines-family/',
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
        data = f'------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n294\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n281\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n1\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\n{target}\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\ntest\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\n{target}\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\n{self.get_text()}\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_schedule"\r\n\r\n\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M\r\nContent-Disposition: form-data; name="wp_iec_term"\r\n\r\n1\r\n------WebKitFormBoundaryLDN4tcKfEzAYr03M--\r\n'
        response = requests.post(url, headers=headers, data=data.encode())
        return response


if __name__ == '__main__':
    project_name = 'vetcards'
    s = 'Thank you'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3Y7xjDx'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
