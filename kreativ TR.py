from threading import Thread

import requests

from module.data import get_text_from_database, get_target_from_database, get_proxy_from_database, try_to, \
    update_target_site


@try_to
def post(email: str, proxy: str, text: str):
    proxy = {'http': proxy, 'https': proxy}
    url = 'https://kreativ-welt.de/wp-json/contact-form-7/v1/contact-forms/20316/feedback'
    headers_in_text = {
        "accept": "application/json, */*;q=0.1",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary1eQJ9B9FhtSCZvy5",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        # "cookie": "_fbp=fb.1.1660986376834.1541713192; __gads=ID=7e7606b5e3a2deb9-22ec8f96f7cd007f:T=1660986376:RT=1660986376:S=ALNI_MaEVTS-H1iAAkwYzwLpq1XeeWrY9Q; __gpi=UID=00000ae1d20ca41f:T=1660986376:RT=1660986376:S=ALNI_Maa-4H1ujo3UqqRGSGKD2DD9myVdA; borlabs-cookie=%7B%22consents%22%3A%7B%22essential%22%3A%5B%22borlabs-cookie%22%5D%2C%22statistics%22%3A%5B%22google-analytics%22%5D%2C%22marketing%22%3A%5B%22google-adsense%22%2C%22facebook-pixel%22%5D%2C%22external-media%22%3A%5B%22facebook%22%2C%22googlemaps%22%2C%22youtube%22%5D%7D%2C%22domainPath%22%3A%22kreativ-welt.crnd.de%2F%22%2C%22expires%22%3A%22Sat%2C%2018%20Feb%202023%2009%3A06%3A19%20GMT%22%2C%22uid%22%3A%22mnep763s-rd6x72ar-cp4vilgp-78z4hijv%22%2C%22version%22%3A%222%22%7D; _ga=GA1.1.639037240.1660986376; _ga_K89QP760VG=GS1.1.1660986376.1.0.1660986379.0.0.0",
        "Referer": "https://kreativ-welt.de/enquiry/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    body = f'------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"_wpcf7\"\r\n\r\n20316\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"_wpcf7_version\"\r\n\r\n5.5.6\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"_wpcf7_locale\"\r\n\r\nde_DE\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"_wpcf7_unit_tag\"\r\n\r\nwpcf7-f20316-p124460-o1\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"_wpcf7_container_post\"\r\n\r\n124460\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"_wpcf7_posted_data_hash\"\r\n\r\n\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"company\"\r\n\r\n{text}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"firstName\"\r\n\r\n{text}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"lastName\"\r\n\r\n{text}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"city\"\r\n\r\n{text}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"country\"\r\n\r\n{text}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n{text}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"mail\"\r\n\r\n{email}\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"website\"\r\n\r\nhttps://kreativ-welt.de/enquiry/\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"standart[]\"\r\n\r\nRow Stand\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"standart[]\"\r\n\r\nCorner Stand\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"standart[]\"\r\n\r\nPeninsular Stand\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"workshop1[]\"\r\n\r\nWe would like to offer a workshop (workshops receive a special offer)\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"width-min\"\r\n\r\n123\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"width-max\"\r\n\r\n123\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"depth-min\"\r\n\r\n123\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"depth-max\"\r\n\r\n213\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"workshop2[]\"\r\n\r\nCar parking permit for exhibition ground\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"workshop3[]\"\r\n\r\nElectricity up to 3 KW\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"workshop4[]\"\r\n\r\nIndividual stand construction\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"specialOffer\"\r\n\r\n2x4 Corner Stand\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"comment\"\r\n\r\n{text} https://kreativ-welt.de/enquiry/\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5\r\nContent-Disposition: form-data; name=\"contact_sendmail[]\"\r\n\r\nPlease send copy to my email address\r\n------WebKitFormBoundary1eQJ9B9FhtSCZvy5--\r\n'
    return requests.post(url, headers=headers_in_text, data=body, proxies=proxy, timeout=10)


def post_text(db_name):
    link = ' shortbit.us/CrfYJ'
    text = get_text_from_database() + link
    target = get_target_from_database(db_name, 'kreativ TR').text
    result = None
    while result is None:  # todo remove that
        proxy = get_proxy_from_database('west_proxy')
        result = post(target, proxy, text)
    test = result.content.decode()
    if 'Thank you for your message.' not in test:
        update_target_site(db_name, target, None)
    return result.content, target


def main():
    while True:
        test = post_text('turk.db')
        print(test)


if __name__ == '__main__':
    threads = []
    for i in range(25):
        thread = Thread(target=main)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
