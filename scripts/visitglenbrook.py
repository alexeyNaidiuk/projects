import requests

from module.spam_abstraction import Spam

url = 'https://visitglenbrook.com/resources/send-a-greeting/'

cookies = {
    'active_demand_cookie_cart': '637e2632b5c16',
    'calltrk_referrer': 'https%3A//www.google.com/',
    'calltrk_landing': 'https%3A//visitglenbrook.com/resources/send-a-greeting/',
    'calltrk_session_id': '03aea7e7-6efd-4fea-ac41-8b322856d0c6',
    'calltrk_fcid': 'f47b29f4-241c-42ef-875c-e30443f4ea13',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryqeCgHAvGYwvpVajH',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'active_demand_cookie_cart=637e2632b5c16; calltrk_referrer=https%3A//www.google.com/; calltrk_landing=https%3A//visitglenbrook.com/resources/send-a-greeting/; calltrk_session_id=03aea7e7-6efd-4fea-ac41-8b322856d0c6; calltrk_fcid=f47b29f4-241c-42ef-875c-e30443f4ea13',
    'Origin': 'https://visitglenbrook.com',
    'Referer': 'https://visitglenbrook.com/resources/send-a-greeting/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

data = '------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n11844\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n11843\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n1\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\ntest \r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\ntest \r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryqeCgHAvGYwvpVajH--\r\n'


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        post_data = data.replace('test', self.get_text()).replace('softumwork@gmail.com', target).encode()
        response = requests.post(url, cookies=cookies, headers=headers, data=post_data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'thankyou_redirect'
    project_name = 'visitglenbrook'
    promo_link = 'bit.ly/3i33mnE'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
