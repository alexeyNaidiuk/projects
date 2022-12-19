import requests

import module

cookies = {
    'PHPSESSID': 'c05ipd906o1h4sm4ssr360tpb7n766ji',
    'wp_woocommerce_session_9ea9d69e9524bd982f6b26e000b57352': 't_8e96fecf85e9afdcdc068e7f79c89f%7C%7C1671617706%7C%7C1671614106%7C%7Cc325bc8b0beb9afda4fe834c45999a34',
    'yith_ywraq_session_9ea9d69e9524bd982f6b26e000b57352': '336cedb127b491f63584fceb11568d07%7C%7C1671617706%7C%7C1671614106%7C%7Cd01e4e14e62d86ddd133da66069fd818',
}

headers = {
    'Accept': 'application/json, */*;q=0.1',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarykS2FI0e83WMkKbil',
    # 'Cookie': 'PHPSESSID=c05ipd906o1h4sm4ssr360tpb7n766ji; wp_woocommerce_session_9ea9d69e9524bd982f6b26e000b57352=t_8e96fecf85e9afdcdc068e7f79c89f%7C%7C1671617706%7C%7C1671614106%7C%7Cc325bc8b0beb9afda4fe834c45999a34; yith_ywraq_session_9ea9d69e9524bd982f6b26e000b57352=336cedb127b491f63584fceb11568d07%7C%7C1671617706%7C%7C1671614106%7C%7Cd01e4e14e62d86ddd133da66069fd818',
    'Origin': 'https://tricomradio.com',
    'Referer': 'https://tricomradio.com/contact/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
DATA = '------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n341\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.1\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f341-p125-o1\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n125\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="text-product"\r\n\r\ntest\r\n------WebKitFormBoundarykS2FI0e83WMkKbil\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundarykS2FI0e83WMkKbil--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target).encode()

        response = requests.post(
            'https://tricomradio.com/wp-json/contact-form-7/v1/contact-forms/341/feedback',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        return response


if __name__ == '__main__':
    project_name = 'tricomradio'
    s = 'It has been sent.'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3hEJQhp'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
