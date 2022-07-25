import requests
from requests_toolbelt import MultipartEncoder

from module.data import generate_proxy, get_proxies, try_to, main

text_body = '''🔥 Herkese verdik! Sana da verelim! 50 TL Casino Bonusu!  https://bit.ly/3aM5iOf'''
proxy_generator = generate_proxy(set(get_proxies(r'proxies_folder/proxies.txt')))


@try_to
def post(target: str, proxy: str = None):
    fields = {
        'input_1': 'A Question',
        'input_2': 'RBT',
        'input_12.1': '1',
        'input_12.2': 'I have reviewed the RBT page and handbook, and I still have a question',
        'input_12.3': '20',
        'input_19': 'Applying to be an RBT',
        'input_23.3': 'name',
        'input_23.6': 'lastname',
        'input_24': target,
        'input_25': '',
        'input_26': text_body,
        'input_43.1': '1',
        'input_43.2': 'I agree to allow the BACB to contact me with the information provided to help with my inquiry.',
        'input_43.3': '20',
        'gform_ajax': 'form_id=75&title=&description=1&tabindex=0',
        'is_submit_75': '1',
        'gform_submit': '75',
        'gform_unique_id': '',
        'state_75': 'WyJ7XCIxMi4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiMTIuMlwiOlwiYWUxZjYyMjM5YTVlNWRiMDhmM2U3NTQ1ZDY4ZWZhYjJcIixcIjEyLjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCIsXCIxMy4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiMTMuMlwiOlwiMDJlYTRhZjM2ZjFhMDJlMTZiOGNiMWVhYjMwM2VmZmNcIixcIjEzLjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCIsXCIxNC4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiMTQuMlwiOlwiMGQyZWMxMmFmNWE4Yjg3MDc2NTFkNGU3NjM3MGYxZDdcIixcIjE0LjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCIsXCI1NC4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiNTQuMlwiOlwiOGI1MmQ4ZTIyODJmMTU2MDUwMDhlZjQxZTAxOTI5MWJcIixcIjU0LjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCIsXCIxNS4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiMTUuMlwiOlwiNmFjOWY4NmY2NmU2ZTM0YWJkNDcwMjA4YmMxOTI4YWZcIixcIjE1LjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCIsXCIxOC4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiMTguMlwiOlwiMWU3YjkxMGY2MDJkZWU1M2E3MTQ0ZWJhMTkxMTNkOTVcIixcIjE4LjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCIsXCI0My4xXCI6XCI2ZjAxOGM5MTYxMThmMjFmZjE5YzgyMjViMDgzZDMyZlwiLFwiNDMuMlwiOlwiMWExYWU1YTY5YTdkMDFhNjk5Zjg5NmQxNTNiOTg2ZDhcIixcIjQzLjNcIjpcIjA5M2ZlOWRmNjUwZDdhZTdkNGM3ZmVjN2VmYjkyYzVjXCJ9IiwiOGFiOThlYWMxYzc4YTA0N2M4NmZhMTUxYzIyMmU2Y2UiXQ==',
        'gform_target_page_number_75': '0',
        'gform_source_page_number_75': '1',
        'gform_field_values': '',
        'gform_uploaded_files': '',
    }
    data = MultipartEncoder(fields=fields)
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": data.content_type,
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "iframe",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    url = 'https://www.bacb.com/contact-us/'
    proxies = {'http': proxy, 'https': proxy}
    return requests.post(url, headers=headers, data=data, proxies=proxies, verify=False, timeout=5)


def spam(target: str):
    result = None
    while result is None:
        proxy = next(proxy_generator)
        result = post(target, proxy)
    return result, target


if __name__ == '__main__':
    # test_main(spam)
    main(spam, 50)
