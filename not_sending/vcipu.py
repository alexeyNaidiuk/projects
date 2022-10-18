from string import Template
import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            'd418c68a2f0889faf8c3546887930649': '6fb5mkjjlm6q772bq3tkttuuu9',
        }

        headers = {
            'authority': 'www.vcipu.cz',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryPw8xCRTPEKp3BrJA',
            'origin': 'https://www.vcipu.cz',
            'referer': 'https://www.vcipu.cz/ru/18-michalska/menyu/98-zakuski-k-pivu',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'format': 'json',
        }

        data = '------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[contact_name]"\r\n\r\ntext\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[contact_email]"\r\n\r\n$target\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[contact_subject]"\r\n\r\nБронирование\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[contact_message]"\r\n\r\n\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[contact_email_copy]"\r\n\r\n1\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[n3t_custom_fields][f0]"\r\n\r\ntext\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[n3t_custom_fields][f1]"\r\n\r\ntext\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[n3t_custom_fields][f2]"\r\n\r\n28.10.2022\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[n3t_custom_fields][f3]"\r\n\r\n11:00\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[n3t_custom_fields][f4]"\r\n\r\n$text\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="jform[captcha][email]"\r\n\r\n\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="option"\r\n\r\ncom_contact\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="task"\r\n\r\ncontact.submit\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="return"\r\n\r\n\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="id"\r\n\r\n6:restaurace-v-cipu-michalska-ru\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA\r\nContent-Disposition: form-data; name="fc0dac9ba04cfd1600036f40bd9c8c38"\r\n\r\n1\r\n------WebKitFormBoundaryPw8xCRTPEKp3BrJA--\r\n'
        data = Template(data).substitute({'text': text, 'target': target})
        response = requests.post('https://www.vcipu.cz/ru/', params=params, cookies=cookies, headers=headers,
                                 data=data.encode().decode('latin-1'), proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = '"success":true'
    project_name = 'vcipu'
    promo_link = 'bit.ly/3STPedP'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
