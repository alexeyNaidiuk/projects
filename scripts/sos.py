from string import Template
import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '_ga': 'GA1.1.394050887.1666083640',
            'optiMonkClientId': '85ec2786-03b6-11c5-19fe-f807ddba9215',
            'PAPVisitorId': 'WgqBbK0esX5agJZ8cF8WPiuGIohE0M90',
            'optiMonkSession': '1666083627',
            'CookieConsent': '{stamp:%27M5G6v4ViS6/joee0OkWLu9xGo91/IewvagV0B8SVZKjb5xIw7NoTKw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1666083836275%2Cregion:%27ua%27}',
            '_fw_crm_v': 'ca170ddd-2f38-4b5c-fa61-f9086b8eae11',
            'stg_returning_visitor': 'Tue%2C%2018%20Oct%202022%2009:04:59%20GMT',
            'stg_traffic_source_priority': '1',
            '_pk_ses.25591afa-0fea-4225-ac18-72832360e405.a7a5': '*',
            'omAbTest29': '631f231647a1df002519331b',
            '_ga_CR0EM09Q5P': 'GS1.1.1666087477.2.1.1666087608.60.0.0',
            'first_session': '%7B%22visits%22%3A10%2C%22start%22%3A1666083851852%2C%22last_visit%22%3A1666087608757%2C%22url%22%3A%22https%3A%2F%2Fsos-wp.it%2Fcontattaci%2F%22%2C%22path%22%3A%22%2Fcontattaci%2F%22%2C%22referrer%22%3A%22https%3A%2F%2Fsos-wp.it%2F%22%2C%22referrer_info%22%3A%7B%22host%22%3A%22sos-wp.it%22%2C%22path%22%3A%22%2F%22%2C%22protocol%22%3A%22https%3A%22%2C%22port%22%3A80%2C%22search%22%3A%22%22%2C%22query%22%3A%7B%7D%7D%2C%22search%22%3A%7B%22engine%22%3Anull%2C%22query%22%3Anull%7D%2C%22prev_visit%22%3A1666087587662%2C%22time_since_last_visit%22%3A21095%2C%22version%22%3A0.4%7D',
            'optiMonkClient': 'N4IgjAbArAnADAZhALlAYwIYtAJhtkDNAFxTgBpCAHKlSCCOADgSaZ0rQCcUQIEwAMxwCIAFgDsGMABNBcODihgYCAQCMQlAHYB7GXUoBnXmgA2uowFMDAX1uVBANzoNGLCDgmUzL5PXcJWDEdXSo/MBx7IA',
            '_pk_id.25591afa-0fea-4225-ac18-72832360e405.a7a5': '42e0ca4e7d59f72e.1666083641.2.1666087623.1666087478.',
            'stg_last_interaction': 'Tue%2C%2018%20Oct%202022%2010:07:03%20GMT',
        }
        headers = {
            'authority': 'sos-wp.it',
            'accept': 'application/json, */*;q=0.1',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryDIw4AvQiMCaEkS5R',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.1.394050887.1666083640; optiMonkClientId=85ec2786-03b6-11c5-19fe-f807ddba9215; PAPVisitorId=WgqBbK0esX5agJZ8cF8WPiuGIohE0M90; optiMonkSession=1666083627; CookieConsent={stamp:%27M5G6v4ViS6/joee0OkWLu9xGo91/IewvagV0B8SVZKjb5xIw7NoTKw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1666083836275%2Cregion:%27ua%27}; _fw_crm_v=ca170ddd-2f38-4b5c-fa61-f9086b8eae11; stg_returning_visitor=Tue%2C%2018%20Oct%202022%2009:04:59%20GMT; stg_traffic_source_priority=1; _pk_ses.25591afa-0fea-4225-ac18-72832360e405.a7a5=*; omAbTest29=631f231647a1df002519331b; _ga_CR0EM09Q5P=GS1.1.1666087477.2.1.1666087608.60.0.0; first_session=%7B%22visits%22%3A10%2C%22start%22%3A1666083851852%2C%22last_visit%22%3A1666087608757%2C%22url%22%3A%22https%3A%2F%2Fsos-wp.it%2Fcontattaci%2F%22%2C%22path%22%3A%22%2Fcontattaci%2F%22%2C%22referrer%22%3A%22https%3A%2F%2Fsos-wp.it%2F%22%2C%22referrer_info%22%3A%7B%22host%22%3A%22sos-wp.it%22%2C%22path%22%3A%22%2F%22%2C%22protocol%22%3A%22https%3A%22%2C%22port%22%3A80%2C%22search%22%3A%22%22%2C%22query%22%3A%7B%7D%7D%2C%22search%22%3A%7B%22engine%22%3Anull%2C%22query%22%3Anull%7D%2C%22prev_visit%22%3A1666087587662%2C%22time_since_last_visit%22%3A21095%2C%22version%22%3A0.4%7D; optiMonkClient=N4IgjAbArAnADAZhALlAYwIYtAJhtkDNAFxTgBpCAHKlSCCOADgSaZ0rQCcUQIEwAMxwCIAFgDsGMABNBcODihgYCAQCMQlAHYB7GXUoBnXmgA2uowFMDAX1uVBANzoNGLCDgmUzL5PXcJWDEdXSo/MBx7IA; _pk_id.25591afa-0fea-4225-ac18-72832360e405.a7a5=42e0ca4e7d59f72e.1666083641.2.1666087623.1666087478.; stg_last_interaction=Tue%2C%2018%20Oct%202022%2010:07:03%20GMT',
            'origin': 'https://sos-wp.it',
            'referer': 'https://sos-wp.it/Temi-Wordpress/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = '------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n107573\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.3\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nit_IT\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f107573-o1\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7cf_hidden_group_fields"\r\n\r\n[]\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7cf_hidden_groups"\r\n\r\n[]\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7cf_visible_groups"\r\n\r\n[]\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7cf_repeaters"\r\n\r\n[]\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7cf_steps"\r\n\r\n{}\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7cf_options"\r\n\r\n{"form_id":107573,"conditions":[],"settings":{"animation":"yes","animation_intime":200,"animation_outtime":200,"conditions_ui":"normal","notice_dismissed":false,"notice_dismissed_rollback-cf7-5.6":true}}\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="cf7-nome"\r\n\r\n$text\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="cf7-email"\r\n\r\n$email\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="acceptance-682"\r\n\r\n1\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_ak_hp_textarea"\r\n\r\n\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="_wpcf7_ak_js"\r\n\r\n1666087608507\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bib"\r\n\r\n1666087614081\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bfs"\r\n\r\n1666087623002\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bkpc"\r\n\r\n7\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bkp"\r\n\r\n154;151,99;129,16;105,8;1;56;64,8;\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bmc"\r\n\r\n80;75,2228;70,345;63,233;85,1675;61,2571;69,1923;80,809;111,3288;\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bmcc"\r\n\r\n9\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bmk"\r\n\r\n\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bck"\r\n\r\n\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bmmc"\r\n\r\n11\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_btmc"\r\n\r\n0\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bsc"\r\n\r\n1\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bte"\r\n\r\n\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_btec"\r\n\r\n0\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R\r\nContent-Disposition: form-data; name="ak_bmm"\r\n\r\n354,1464;112,21;183,1418;308,1324;284,3;1191,1578;984,6;1185,207;2515,67;64,54;72,15;\r\n------WebKitFormBoundaryDIw4AvQiMCaEkS5R--\r\n'
        data = Template(data).substitute({'text': text, 'email': target})
        response = requests.post('https://sos-wp.it/wp-json/contact-form-7/v1/contact-forms/107573/feedback',
                                 cookies=cookies, headers=headers, data=data, proxies=proxies)

        return response


if __name__ == '__main__':
    success_message = 'Grazie per il tuo messaggio'
    project_name = 'sos'
    promo_link = 'bit.ly/3s1jjMO'
    spam = ConcreteSpam(promo_link, project_name, success_message, text_encoding='latin-1', with_stickers=False)
    res = spam.send_post(target='softumwork+16@gmail.com')
    # if res:
    #     spam.run_concurrently()
