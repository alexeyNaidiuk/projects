import requests

from module.data import target_generator, try_to

TEXT = '🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://cutt.ly/SZnNqlC'


@try_to
def post(target: str):
    url = 'https://my.flipdish.com/feedmefast/contact'
    headers = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }

    data = {
        'Name': TEXT * 4,
        'Phone': TEXT * 100,
        'Email': target,
        'Captcha': '4',
        'message': TEXT,
        'X-Requested-With': 'XMLHttpRequest'
    }

    res = requests.post(url, data, headers=headers)
    return res


def spam(target='softumwork@gmail.com'):
    res = None
    while res is None:
        res = post(target)
    return res, target


if __name__ == '__main__':
    test = spam()
    print(test)
    for target in target_generator(r'C:\Users\Admin\Desktop\projects\targets\all_turk.csv'):
        print(spam(target))
