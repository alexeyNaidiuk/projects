from string import Template

import requests

from module.spam_abstraction import Spam

url = 'https://www.anox.fr/en/module/roja45quotationspro/QuotationsProFront'

cookies = {
    'PHPSESSID': '29had7aimls2lvmqdfoc3f8jg6',
    'PrestaShop-a6530979075b9500fc98d5958ea98ffb': 'def50200ba1644439c6f8d353fe3e5bafde5bc1730182abd3bd2e123142b8fbaec560eeb94cdf6a82203d3a66ecd84a71d4616dd2f0538965d507c338c3ce4405270648b123d6b2a208c1d1fcbd0bce8618e128623379011fbc849ec8439c948dc1afff211db40bb21b5035c72e3a170ec8fc4461cb767b54a1538dc6e2b0d38a2e733ebd63e6d344861ee49f534efc44c4d43edbfdd75df5b38fed89f42274cab17550cca8d99411fbd8ababfd0267e7abdfcefeaac6cb477fe6b44996a019cdde7560b170df6c6211debc1eaaf479b8bc355578f79f5f74dbf966af1a250b68acb9c41ce152b67fde76a8e3d156722484db5cc26e22358a2d475a9da9d0edcf16e4d',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3H0453jb1PyCtmXX',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=29had7aimls2lvmqdfoc3f8jg6; PrestaShop-a6530979075b9500fc98d5958ea98ffb=def50200ba1644439c6f8d353fe3e5bafde5bc1730182abd3bd2e123142b8fbaec560eeb94cdf6a82203d3a66ecd84a71d4616dd2f0538965d507c338c3ce4405270648b123d6b2a208c1d1fcbd0bce8618e128623379011fbc849ec8439c948dc1afff211db40bb21b5035c72e3a170ec8fc4461cb767b54a1538dc6e2b0d38a2e733ebd63e6d344861ee49f534efc44c4d43edbfdd75df5b38fed89f42274cab17550cca8d99411fbd8ababfd0267e7abdfcefeaac6cb477fe6b44996a019cdde7560b170df6c6211debc1eaaf479b8bc355578f79f5f74dbf966af1a250b68acb9c41ce152b67fde76a8e3d156722484db5cc26e22358a2d475a9da9d0edcf16e4d',
    'Origin': 'https://www.anox.fr',
    'Referer': 'https://www.anox.fr/en/module/roja45quotationspro/QuotationsProFront?action=quoteSummary&module=roja45quotationspro',
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


class ConcreteSpam(Spam):

    def post(self, text, target) -> requests.Response:


        data = '------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="action"\r\n\r\nsubmitRequest\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_FORMDATA"\r\n\r\n{"columns":[{"heading":"","num":1,"fields":[{"pos":0,"name":"ROJA45QUOTATIONSPRO_FIRSTNAME","type":"TEXT","label":"First Name","value":"test"},{"pos":1,"name":"ROJA45QUOTATIONSPRO_LASTNAME","type":"TEXT","label":"Last Name","value":"test"},{"pos":2,"name":"ROJA45QUOTATIONSPRO_EMAIL","type":"TEXT","label":"Email Address","value":"softumwork@gmail.com"},{"pos":3,"name":"ROJA45QUOTATIONSPRO_VotreRefDeDemande","type":"TEXT","label":"","value":"$text"},{"pos":4,"name":"ROJA45QUOTATIONSPRO_Message","type":"TEXTAREA","label":"","value":"test"},{"pos":5,"name":"Code_Postal_Livraison","type":"TEXT","label":"","value":"test"},{"pos":6,"name":"Pays_de_livraison","type":"COUNTRY","label":"","value":"Allemagne","id":"1"}]},{"fields":[]}]}\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_FIRSTNAME"\r\n\r\ntest\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_LASTNAME"\r\n\r\ntest\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_EMAIL"\r\n\r\nsoftumwork@gmail.com\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_VotreRefDeDemande"\r\n\r\n$text\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_Message"\r\n\r\n$text\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="Code_Postal_Livraison"\r\n\r\ntest\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="Pays_de_livraison"\r\n\r\n1\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="UploadReceipt"\r\n\r\n1\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="uploadedfile[]"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundary3H0453jb1PyCtmXX\r\nContent-Disposition: form-data; name="ROJA45QUOTATIONSPRO_CUSTOMER_COPY"\r\n\r\non\r\n------WebKitFormBoundary3H0453jb1PyCtmXX--\r\n'
        data = data.replace('softumwork@gmail.com', target)
        data = Template(data).substitute({'text': text.encode().decode('latin-1')})
        response = requests.post(url, cookies=cookies, headers=headers, data=data, proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Thank You.'
    project_name = 'anox'
    promo_link = 'bit.ly/3EBl36B'
    spam = ConcreteSpam(promo_link, project_name, success_message, with_stickers=False)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
