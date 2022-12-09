import requests

import module

url = 'https://asadatec.de/en/component/convertforms'
headers = {
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryoEoow4yGnuw0pjJi',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
params = {
    'task': 'submit',
}
DATA = '------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[firstname]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[lastname]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[company]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[street]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[zipcode]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[city]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[country]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[email]"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[telephone]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[dropdown]"\r\n\r\nby another company\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[comment]"\r\n\r\ntest\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[privacy][]"\r\n\r\nI have read the terms of privacy and accept them\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[service][]"\r\n\r\nI accept the terms of service of ASA Datec Datensysteme GmbH\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[copy][]"\r\n\r\nSend copy to me\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[form_id]"\r\n\r\n3\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="2a8739eaeb2fafc5c7476755850c5501"\r\n\r\n1\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi\r\nContent-Disposition: form-data; name="cf[hnpt]"\r\n\r\n\r\n------WebKitFormBoundaryoEoow4yGnuw0pjJi--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('softumwork@gmail.com', target).replace('test', self.get_text())
        response = requests.post(url, params=params, headers=headers, data=data.encode())
        return response


if __name__ == '__main__':
    project_name = 'asadatec'
    s = '"success":true'

    project = 'fortuneclock'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3UNEtKe'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
