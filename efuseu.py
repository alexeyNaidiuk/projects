from concurrent.futures import ThreadPoolExecutor

from requests import Session
from spintax import spintax
from data import SOLVER, subject, text_body, get_targets

sitekey = '6LdNeDUUAAAAABpwRBYbCMJvQoxLi4d31Oho0EBw'


def get(s: Session, url: str):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'utf-8',
        "Accept-Language": 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        "Connection": 'keep-alive',
        'Host': 'efus.eu',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows"
    }

    response = s.get(url, headers=headers, timeout=5)
    return response


def post(s: Session, email, subbject, text_body, captcha_response):

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': '',
        'Origin': 'https://efus.eu',
        'Referer': 'https://efus.eu/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'CONTACT_EMAIL': email,
        'FIRSTNAME': subbject,
        'LASTNAME': text_body,
        'CONTACT_CF60': 'Institution ',
        'JOB_TITLE': 'Job title  ',
        'COUNTRY': 'USA',
        'CONTACT_CF61': 'English',
        'g-recaptcha-response': captcha_response,
        'listCheckBox': '50428000001144041',
        'SIGNUP_SUBMIT_BUTTON': 'Subscribe',
        'zc_trackCode': 'ZCFORMVIEW',
        'viewFrom': 'URL_ACTION',
        'submitType': 'optinCustomView',
        'lD': '1b327ffb2c61871',
        'zx': '11d852f3',
        'zcvers': '3.0',
        'mode': 'OptinCreateView',
        'zcld': '1b327ffb2c61871',
        'zc_formIx': '3zd6799c593c6dc19618640b6f0a24f7c24c4893b9051db5bc6f3fad4bba908bc3',
        'lf': '1657786683643',  # var
        'di': '114861821023093825871657786683645',  # var
        'responseMode': 'inline',
        'sourceURL': 'https://efus.eu/subscribe-to-newsletter/',
        'tpIx': '3z05f2cd4ec9a4363d2c44aca5344f5f97e95d8f8f1e7ae03788fc08d326f2e4f1',  # var
        'custIx': '3z17fcb662426f5844728355040bef8f146dae4cbf828d3f86b833379f7ff3ffde',  # var
    }

    response = s.get('https://vxhi.maillist-manage.com/weboptin.zc', params=params, headers=headers)
    return response


def spam(email):
    url = 'https://efus.eu/subscribe-to-newsletter/'
    s = Session()
    r = get(s, url=url)
    print(r)
    captcha_answer = SOLVER.recaptcha(sitekey=sitekey, url=url)
    print(captcha_answer)
    r = post(s, email=email,
             subbject=spintax.spin(subject),
             text_body=spintax.spin(text_body),
             captcha_response=captcha_answer['code'])
    print(r)


def main():
    targets = get_targets()
    with ThreadPoolExecutor(max_workers=1000) as worker:
        worker.map(spam, targets)


def test():
    spam('alexeynaidiuk@gmail.com')


if __name__ == '__main__':
    test()
