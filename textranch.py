import requests


def post():

    cookies = {
        'csrftoken': '5sSFUiM9crKczycvjiR2BJteYdEKN5OKnBW2zKDZELRkUItZrnWNGepPD1vey16Q',
        'sessionid': 'eqj14nhpvxtlxs3issadl3xhlktww2eh',
        'ac_enable_tracking': '1',
        '_iub_cs-40750572': '%7B%22consent%22%3Atrue%2C%22timestamp%22%3A%222022-07-12T10%3A22%3A49.904Z%22%2C%22version%22%3A%220.11.36.4%22%2C%22id%22%3A40750572%7D',
        'hide_banner_july2022': '1',
    }

    headers = {
        'authority': 'textranch.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://textranch.com',
        'referer': 'https://textranch.com/166020/sent-us-an-email/or/send-an-email-to-us/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        # 'x-csrftoken': '5sSFUiM9crKczycvjiR2BJteYdEKN5OKnBW2zKDZELRkUItZrnWNGepPD1vey16Q',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'name': 'without cookies',
        'email': 'softumwork@gmail.com',
        'ref_form': 'lead_gen_internal_pages_bottom',
    }

    response = requests.post('https://textranch.com/optin-users/',
                             # cookies=cookies,
                             headers=headers, data=data)
    return response


def main():
    r = post()
    print(r.content)


if __name__ == '__main__':
    main()
