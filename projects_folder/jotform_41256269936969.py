import requests

from projects_folder.module.data import generate_proxy, get_proxies, try_to, test_main, main

proxy_generator = generate_proxy(set(get_proxies(r'C:\Users\Admin\Desktop\projects\proxies_folder\proxies.txt')))


@try_to
def post(target, proxy=None):
    url = 'https://submit.jotformpro.com/submit/41256269936969/'
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
        'formID': '41256269936969',
        'q132_name132[]': 'In+Person+@+WIPO+(for+registered+observers+and+delegates+only)',
        'q62_fullName62[first]': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q62_fullName62[last]': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q6_title': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q7_organization7': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q17_email17': target,
        'q8_address8': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q10_city': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q11_stateprovince': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'q12_zippostalCode': '12421', 'q13_country': 'USA', 'q14_phone14': '12451212',
        'q124_name124[other]': 'other',
        'q128_specialRequests128': '🔥Herkese verdik!Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf',
        'website': '', 'simple_spc': '41256269936969-41256269936969',
        'event_id': '1658749056431_41256269936969_VFCZPcC'
    }
    resp = requests.post(url, headers=headers, data=data, proxies={'http': proxy, 'https': proxy}, timeout=5,
                         verify=False)
    return resp


def spam(target):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        post_resp = post(target=target, proxy=proxy)
        if post_resp:
            if 'captcha' not in post_resp.text:
                result = post_resp
    return result, target


if __name__ == '__main__':
    test_main(spam)
    main(spam, 5)
