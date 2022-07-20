from concurrent.futures import ThreadPoolExecutor
from random import choice

import spintax
from requests import Session

subject = '''{Your|The} 50 {FS|freespins|free spins|spins} {is|are} {ready|waiting}{!|}'''
text_body = '''{Get|Loot|Use} {your|} 50 {FS|freespins|free spins|spins} for a {quick Registration|start|take a part} on FortuneClock by {clicking|following|coming} the {link|url} below https://referencemen.com/ktVmDV?c=0097xLek_pT9MB058910793879e922&utm_source=333 {Hurry up!|Get a move on!|Rush!} This {offer|promo|stock} is limited in time! {Your|The} 50 {FS|freespins|free spins|spins} {is|are} {ready|waiting}{!|}'''


def get(s: Session, proxy=None):
    # cookies = {
    #     'ecsi': '%7B%22https%3A%2F%2Fec.europa.eu%2Fwel%2Fsurveys%2Fwr_survey03%2Fdata%2Finvitation_settings%2Feu_online_survey%2F01%2Finvitation_settings.js%22%3A%7B%22de%22%3A%7B%22show_welcome_pop_up%22%3Afalse%2C%22show_reminder_pop_up%22%3Afalse%7D%7D%7D',
    #     'cck1': '%7B%22cm%22%3Atrue%2C%22all1st%22%3Atrue%2C%22closed%22%3Atrue%7D',
    # }

    headers = {
        'authority': 'european-union.europa.eu',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ecsi=%7B%22https%3A%2F%2Fec.europa.eu%2Fwel%2Fsurveys%2Fwr_survey03%2Fdata%2Finvitation_settings%2Feu_online_survey%2F01%2Finvitation_settings.js%22%3A%7B%22de%22%3A%7B%22show_welcome_pop_up%22%3Afalse%2C%22show_reminder_pop_up%22%3Afalse%7D%7D%7D; cck1=%7B%22cm%22%3Atrue%2C%22all1st%22%3Atrue%2C%22closed%22%3Atrue%7D',
        'if-modified-since': 'Wed, 13 Jul 2022 13:03:16 GMT',
        'if-none-match': '"1657717396-gzip"',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36',
    }

    response = s.get('https://european-union.europa.eu/contact-eu/write-us_de', headers=headers,
                     proxies={'https': proxy, 'http': proxy}, timeout=5)
    return response


def post(s, email, subject, text_body, proxy=None):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br ',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0 ',
        'Connection': 'keep-alive',
        'Content-Length': '239',
        'Content-Type': 'application/json',
        'Host': 'webtools.ec.europa.eu',
        'Origin': 'https://forms-edcc.conectys.com',
        'Referer': 'https://forms-edcc.conectys.com/',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
    }

    payload = {
        'form_tools_form_id': '1723',
        'lang': 'de',
        'firstName': 'David',
        'lastName': 'Cooper',
        'emailAddress': email,
        'nationality': 'Ukrainian',
        'countryOfResidence': 'Ukraine',
        'preferredContactLanguage': 'en',
        'alternativeContactLanguage': 'en',
        'enquiry': text_body,
        'europeMailingList': 'true'
    }

    response = s.post('https://webtools.ec.europa.eu/form-tools/process.php', headers=headers,
                      json=payload,
                      proxies={'https': proxy, 'http': proxy})
    return response

def get_proxies() -> list:
    with open(r'C:\Users\Admin\Desktop\projects\proxies.txt', encoding='utf-8') as f:
        return f.read().splitlines()


proxies = get_proxies()


def get_targets() -> list:
    with open(r'C:\Users\Admin\Desktop\projects\emails.txt', encoding='utf-8') as f:
        return f.read().split('\n')


def check_proxy(s, proxy):
    try:
        response = get(s, proxy)
        return response
    except Exception as error:
        proxies.remove(proxy)
        return error


def check_post(s, email: str, proxy: str):
    try:
        r = post(s, email, spintax.spin(subject), spintax.spin(text_body), proxy)
        if not isinstance(r, Exception):
            return r
    except Exception as error:
        return error


def spam(target: str):
    result = False

    while result is False:
        proxy = choice(proxies)
        s = Session()
        r = check_proxy(s, proxy)
        print(r)
        if not isinstance(r, Exception):
            r = check_post(s, target, proxy)
            print(target, r)
            result = True


def main():
    targets = get_targets()
    spam('softumwork@gmail.com')
    # with ThreadPoolExecutor(max_workers=10000) as worker:
    #     worker.map(spam, targets)


if __name__ == '__main__':
    main()
