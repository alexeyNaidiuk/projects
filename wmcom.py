import requests

from data import get_proxies, generate_proxy

all_proxies = get_proxies(r'C:\Users\Admin\Desktop\projects\west_proxy.txt')
proxy_generator = generate_proxy(all_proxies)


def get(proxy):
    url = "https://www.wm.com/ca/en/support/customer-support/contact-us-form"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        # "if-none-match": "\"3674-5e42ecf624d32\"",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        # "cookie": "WMPRD2-HTTPS-Cookie=!h4FElVXd6QleMSQug3LwfZVrjCqilltJ9zedEzO22bym2/An9jt6+dBjK5IBqdePeF3L5f/O1Q0vzLM=; check=true; AMCVS_A8C23BC75245B0200A490D4D%40AdobeOrg=1; _ju_dm=cookie; _ju_dn=1; _ALGOLIA=anonymous-f95193b7-f7cd-4f16-a0a8-44a2d4423c4b; _ju_dc=c2125347-077a-11ed-bdf8-7507a823bb6d; wmdemo=[\"0\"]; AMCV_A8C23BC75245B0200A490D4D%40AdobeOrg=1075005958%7CMCIDTS%7C19193%7CMCMID%7C91123961150848733325342033398160342544%7CMCAID%7CNONE%7CMCOPTOUT-1658308104s%7CNONE%7CvVersion%7C4.4.1; mbox=PC#4e7b3245f475479084a0afe1109d09e6.37_0#1721545706|session#33886dbecf6948dc84e858016aba08ff#1658302765; AWSALB=bu7wftyizrpCfjI3yZf+gkDn43lrbdnc7ahmx/BtAp1uC6kyp5pT4OU6Jc38DIsWqDlxltXPHFHB925C41d0kujbjOTR8uka8FzEnZ9c32MKJhEmWrdanBBNtzh4; AWSALBCORS=bu7wftyizrpCfjI3yZf+gkDn43lrbdnc7ahmx/BtAp1uC6kyp5pT4OU6Jc38DIsWqDlxltXPHFHB925C41d0kujbjOTR8uka8FzEnZ9c32MKJhEmWrdanBBNtzh4; TS0178cdfe=01622743a78ff6fbe5fd3d4a1001398fbb1657f22fc2e5bc8c011f6f9ffd8c3f8f029e29f56512f631cf54451deb897036a5a7465e85d9412cffbc53ff66b67e49d8bf4186bde54425a3a09acf587fc63c5007f61fd4cba4697006a2012f0a3059c08a27fe"
    }
    get_resp = requests.get(url, headers=headers, verify=False)
    return get_resp


def post(target: str, proxy):
    url = "https://rest-api.wm.com/user-request-service?userId=&lang=en_CA"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://www.wm.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "apikey": "E0008A94C99903B68AB5",
    }
    body = {
        "request_type": "SERVICE_REQUEST",
        "product_type": "Contact Us",
        "customerId": "",
        "lob": "R",
        "contact_name": "test",
        "organization_name": "",
        "contact_phone": "",
        "contact_mobile": "",
        "contact_email": target,
        "address": {"street_address": "address", "postal_code": "65651", "state": "AL", "city": "city"},
        "comments": "testBody requests"
    }
    post_resp = requests.post(url, headers=headers, data=body)
    return post_resp


def spam():

    proxy = next(proxy_generator)
    proxy_dict = {'http': proxy, 'https': proxy}

    get_resp = get(proxy_dict)
    print(get_resp)
    post_resp = post('worksoftum@gmail.com', proxy_dict)
    print(post_resp)


if __name__ == '__main__':
    spam()
