import requests

import module

url = 'http://www.villailenia.eu/wp-json/contact-form-7/v1/contact-forms/5/feedback'

headers = {
    'Accept': 'application/json, */*;q=0.1',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryBGPwBxYXN4XhUDNu',
    'Origin': 'http://www.villailenia.eu',
    'Referer': 'http://www.villailenia.eu/contact/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = '------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n5\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6.1\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f5-p48-o1\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n48\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\ne6b44d184fadf12d65c7963e38d00eae\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="your-name"\r\n\r\ntest\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\ntest\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu\r\nContent-Disposition: form-data; name="your-message"\r\n\r\ntest\r\n------WebKitFormBoundaryBGPwBxYXN4XhUDNu--\r\n'
        data = data.replace('test', self.get_text()).replace('softumwork@gmail.com', target).encode()
        response = requests.post(url, headers=headers, data=data, verify=False)
        return response


if __name__ == '__main__':
    project_name = 'villailenia'
    s = 'Grazie per averci contattato'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3PET9u8'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
