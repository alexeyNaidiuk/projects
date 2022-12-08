import requests

import module

url = 'https://forms.hsforms.com/submissions/v3/public/submit/formsnext/multipart/498900/809355fb-b59f-4608-a4bb-0e161053b198'

DATA = '------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="firstname"\r\n\r\ntest\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="lastname"\r\n\r\ntest\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="friend_first_name"\r\n\r\ntest\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="friend_last_name"\r\n\r\ntest\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="friend_email"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan\r\nContent-Disposition: form-data; name="hs_context"\r\n\r\n{"formTarget":"#hbspt-form-ebd722a8-150c-4efa-9442-79d610125448","pageUrl":"https://www.beckershospitalreview.com/invite-friend-subscribe.php","pageTitle":"Invite a Friend","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36","timestamp":1670501076232,"originalEmbedContext":{"portalId":"498900","formId":"809355fb-b59f-4608-a4bb-0e161053b198","region":"na1","target":"#hbspt-form-ebd722a8-150c-4efa-9442-79d610125448","isBuilder":false,"isTestPage":false,"pageTitle":"Invite a Friend","pageUrl":"https://www.beckershospitalreview.com/invite-friend-subscribe.php","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"},"correlationId":"ebd722a8-150c-4efa-9442-79d610125448","lang":"en","embedAtTimestamp":"1670501056241","formDefinitionUpdatedAt":"1597668979084","renderedFieldsIds":["email","firstname","lastname","friend_first_name","friend_last_name","friend_email"],"captchaStatus":"NOT_APPLICABLE","isInsideCrossOriginFrame":false,"source":"forms-embed-1.2450","sourceName":"forms-embed","sourceVersion":"1.2450","sourceVersionMajor":"1","sourceVersionMinor":"2450"}\r\n------WebKitFormBoundaryKU2w0fJ5jCaU0Tan--\r\n'
headers = {
    'authority': 'forms.hsforms.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryKU2w0fJ5jCaU0Tan',
    'origin': 'https://www.beckershospitalreview.com',
    'referer': 'https://www.beckershospitalreview.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        data = DATA.replace('test', self.get_text()).replace('softumwork@gmail.com', target)
        response = requests.post(
            url,
            headers=headers,
            data=data.encode(),
        )
        return response


if __name__ == '__main__':
    project_name = 'hsforms'
    s = 'Thank you!'

    project = 'allright'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3FdWmfG'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
