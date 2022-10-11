from string import Template
import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'cl4859u0p10c58_uid': 'cl4859u0p10c58dd6a3e48-bea4-4bad-9773-7dba8fb5430a',
            'cl4859u0p10c58_gid': 'cl4859u0p10c58af456277-26ee-4984-a28b-8b6e49ac1630',
            'cl4859u0p10c58_eidsTracked': 'true',
            'pum-48454': 'true',
            'cl4859u0p10c58_source': 'www.google.com',
            'cl4859u0p10c58_session_starts': '1665139481341',
            'cl4859u0p10c58_utmParams': '%7B%22utm_source%22%3A%22www.google.com%22%2C%22utm_medium%22%3A%22Organic%20Search%22%2C%22utm_cl_referrer_path%22%3A%22www.google.com%2F%22%2C%22utm_cl_sub_domain%22%3A%22www.google.com%22%7D',
            'cl4859u0p10c58_sid': 'CL-6c1d7f57-cfb2-475c-ace0',
            '_gid': 'GA1.2.2029622154.1665139482',
            '_ga_T6FB36GHX4': 'GS1.1.1665139481.2.1.1665139595.0.0.0',
            '_ga': 'GA1.2.1146101169.1663158823',
            'cl4859u0p10c58_session_ends': '1665141396544',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryh3ifWUZOFDLAOApP',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'cl4859u0p10c58_uid=cl4859u0p10c58dd6a3e48-bea4-4bad-9773-7dba8fb5430a; cl4859u0p10c58_gid=cl4859u0p10c58af456277-26ee-4984-a28b-8b6e49ac1630; cl4859u0p10c58_eidsTracked=true; pum-48454=true; cl4859u0p10c58_source=www.google.com; cl4859u0p10c58_session_starts=1665139481341; cl4859u0p10c58_utmParams=%7B%22utm_source%22%3A%22www.google.com%22%2C%22utm_medium%22%3A%22Organic%20Search%22%2C%22utm_cl_referrer_path%22%3A%22www.google.com%2F%22%2C%22utm_cl_sub_domain%22%3A%22www.google.com%22%7D; cl4859u0p10c58_sid=CL-6c1d7f57-cfb2-475c-ace0; _gid=GA1.2.2029622154.1665139482; _ga_T6FB36GHX4=GS1.1.1665139481.2.1.1665139595.0.0.0; _ga=GA1.2.1146101169.1663158823; cl4859u0p10c58_session_ends=1665141396544',
            'Origin': 'https://allthingscruise.com',
            'Referer': 'https://allthingscruise.com/cruise-e-cards/bon-voyage/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = '------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_img"\r\n\r\n39461\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_post"\r\n\r\n39389\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_unique_id"\r\n\r\n0\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_ajax_validated"\r\n\r\n1\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_action"\r\n\r\nprocess_from\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_name"\r\n\r\n$text\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_email"\r\n\r\n$target\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_fname"\r\n\r\n$text\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_femail"\r\n\r\n$target\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_more_recipient[0][name]"\r\n\r\n\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_more_recipient[0][email]"\r\n\r\n\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_message"\r\n\r\n$text\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP\r\nContent-Disposition: form-data; name="wp_iec_scopy"\r\n\r\n1\r\n------WebKitFormBoundaryh3ifWUZOFDLAOApP--\r\n'
        data = Template(data).substitute({'target': target, 'text': text})
        response = requests.post('https://allthingscruise.com/cruise-e-cards/bon-voyage/', cookies=cookies,
                                 headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank You!'
    project_name = 'allthingscruise'
    promo_link = 'bit.ly/3fSW70F'
    spam = ConcreteSpam(promo_link, project_name, success_message, text_encoding='latin-1')
    res = spam.send_post()
    if res:
        spam.run_concurrently()
