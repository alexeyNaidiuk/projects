import requests

from module import Spam

cookies = {
    'BIGipServerDRUPAL-443': '1068619908.47873.0000',
    '_gid': 'GA1.2.2062439214.1666366765',
    'webform-3028[1666366764]': '1666366764',
    '_ga_YGN990TBJK': 'GS1.1.1666366764.1.1.1666366966.60.0.0',
    '_ga': 'GA1.2.1908910.1666366765',
    '_gat_gtag_UA_26739495_1': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'https://www.mcgill.ca',
    'Referer': 'https://www.mcgill.ca/servicepoint/alumni-contact-form',
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

url = 'https://www.mcgill.ca/servicepoint/alumni-contact-form'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = {
            'submitted[name]': 'text',
            'submitted[mcgill_id_number]': 'text',
            'submitted[email_address]': target,
            'submitted[submit_your_question_below]': text,
            'details[sid]': '',
            'details[page_num]': '1',
            'details[page_count]': '1',
            'details[finished]': '0',
            'form_build_id': 'form-QR--WCjGaIXJpZ9qp_QYrYZg1DR31kZLehBBpDjQBeE',
            'form_id': 'webform_client_form_3028',
            'honeypot_time': '1666366952|OZV1nrlOywqUY-AAhYSZpVSuOFBWkqjccDrerNpmP3g',
            'name': '',
            'op': 'Submit',
        }
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you for your email. We will respond to you within 3-5 working days.'
    project_name = 'mcgill'
    promo_link = 'bit.ly/3z0wMsa'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(7)
