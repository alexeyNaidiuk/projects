import requests
from seleniumwire.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_MANAGER__INSTALL_ = ChromeDriverManager().install()


def get(proxy=None) -> str:
    url = "https://eu.mountainbuggy.com/pages/contact-us-form"
    opts = ChromeOptions()
    driver = Chrome(DRIVER_MANAGER__INSTALL_, options=opts)
    driver.get(url)
    driver_execute_script = driver.execute_script(
        'return localStorage.getItem("fd_0bdb0786-b5e2-4165-b6b7-ab1e99bb35ed_")')
    return driver_execute_script


def post(id, target='softumwrok@gmail.com', proxy=None):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        'accept-encoding': 'gzip, deflate, br',
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://eu.mountainbuggy.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36'
    }

    body = {
        "Brand": "phil&teds",
        "First Name": "name",
        "LastName": "lastname",
        "Email": "softumwork@gmail.com",
        "Phone1": "12151212",
        "Country": "Ukraine",
        "Subject": "subject request",
        "Question": "body request", "Attachments1": [],
        "__id": id
    }
    url = f'https://forms.plumsail.com/api/form/0bdb0786-b5e2-4165-b6b7-ab1e99bb35ed/{id}'
    post_resp = requests.post(url, headers=headers, data=body)
    return post_resp


def spam():
    get_resp = get().replace('"', '')
    post_resp = post(get_resp)
    print(post_resp.json())


if __name__ == '__main__':
    spam()
