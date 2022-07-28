import requests

from projects_folder.module.data import get_proxies, generate_proxy, test_main, try_to, main, get_proxies_from_json

proxy_generator = generate_proxy(set(get_proxies(r'C:\Users\Admin\Desktop\projects\proxies_folder\bad_proxies.txt')))


@try_to
def post(target: str, proxy: str = None):
    url = 'https://submit.jotformpro.com/submit/211176854458160/'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    data = {
        'q58_lenderEmail': target,
        'formID': '211176854458160',
        'q34_lenderName[first]': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q34_lenderName[last]': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q59_lenderNumber[full]': '(124) 412-4124',
        'q52_loanType': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q53_borrowerLast': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q55_maxLoan': '11111',
        'q69_debtTo': '1243412',
        'q68_qualificationNotes': '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'simple_spc': '211176854458160-211176854458160',
        'event_id': '1658757360475_211176854458160_eS48bY9',
        'temp_upload_folder': '211176854458160_62dea0f074f8a'
    }
    proxies = {'http': proxy, 'https': proxy}
    resp = requests.post(url, headers=headers, data=data, proxies=proxies, verify=False)
    return resp


def spam(target: str):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        post_resp = post(target, proxy)
        if post_resp and 'captcha' not in post_resp.text:
            result = post_resp
    return result, target


if __name__ == '__main__':
    test_result = spam('softumwork@gmail.com')
    print(test_result)
    main(spam, 10)
