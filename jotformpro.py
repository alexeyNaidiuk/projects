import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

from bs4 import BeautifulSoup
import requests
from requests_toolbelt import MultipartEncoder
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.webdriver import Service
from webdriver_manager.chrome import ChromeDriverManager

from data import get_targets, get_proxies, generate_proxy, text_body, get_proxy_file_extension

all_proxies = get_proxies(r'C:\Users\Admin\Desktop\projects\west_proxy.txt')

driver_path = ChromeDriverManager().install()


def get(proxy):
    proxy_file_extension = get_proxy_file_extension(proxy.replace('http://', ''))
    url = "https://form.jotformpro.com/71511869968977"
    options = ChromeOptions()
    options.headless = False
    options.add_extension(proxy_file_extension)
    driver = Chrome(service=Service(driver_path), options=options)
    driver.get(url)
    return driver.page_source


def post(target, event_id: str, temp_upload_folder: str, proxy=None):
    url = 'https://submit.jotformpro.com/submit/71511869968977/'
    data = MultipartEncoder(
        fields={
            'formID': (None, '71511869968977', None),
            'input_language': (None, 'English (US)', None),
            'q3_name[first]': (None, text_body, None),
            'q3_name[last]': (None, text_body, None),
            'q4_email': (None, target, None),
            'q5_message': (None, text_body, None),
            'file': (None, None, None),
            'website': (None, None, None),
            'simple_spc': (None, '71511869968977-71511869968977', None),
            'event_id': (None, event_id, None),  # var
            'temp_upload_folder': (None, temp_upload_folder, None)  # var
        }
    )
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": data.content_type,
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        # "cookie": "userReferer=https%3A%2F%2Fform.jotformpro.com%2F; theme=tile-black; guest=guest_fa0353d8bf6a3368; language=ru-RU",
        "Referer": "https://form.jotformpro.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    resp = requests.post(url, headers=headers, data=data, proxies={'http': proxy, 'https': proxy})
    return resp


def try_to_post(result, target, proxy, event_id, temp_upload_folder):
    try:
        result = post(target=target, event_id=event_id, temp_upload_folder=temp_upload_folder, proxy=proxy)
    except Exception as e:
        logging.error(e)
    finally:
        return result


def spam(target: str):
    result = None
    while result is None:
        proxy = next(generate_proxy(all_proxies))
        get_response = get(proxy)
        soup = BeautifulSoup(get_response, 'lxml')
        event_id = soup.find('input', {'name': 'event_id'}).get('value')
        temp_upload_folder = soup.find('input', {'name': 'temp_upload_folder'}).get('value')
        result = try_to_post(result, target, proxy, event_id, temp_upload_folder)
    return result, target


def main():
    with ThreadPoolExecutor(max_workers=15) as worker:
        futures = []
        for target in get_targets(r'C:\Users\Admin\Desktop\projects\all_turk.csv'):
            future = worker.submit(spam, target)
            futures.append(future)
        for future in as_completed(futures):
            future.result()


def test():
    print(spam('softumwork@gmail.com'))


if __name__ == '__main__':
    test()
