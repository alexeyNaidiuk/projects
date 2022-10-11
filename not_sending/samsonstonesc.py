from string import Template

import requests

from module import Spam


class ConcreteSpam(Spam):

    def post(self, text, target, proxies) -> requests.Response:
        cookies = {
            '.ASPXANONYMOUS': 'AdkOxdLZix4xZDMxNzNkMC1kZTkxLTRjNDEtYWFhZC00ZTExZjVmN2ZmNWQ1',
            'language': 'en-US',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryEuuJHgQMGPchcHvp',
            # Requests sorts cookies= alphabetically
            # 'Cookie': '.ASPXANONYMOUS=AdkOxdLZix4xZDMxNzNkMC1kZTkxLTRjNDEtYWFhZC00ZTExZjVmN2ZmNWQ1; language=en-US',
            'Origin': 'http://samsonstonesc.com',
            'Referer': 'http://samsonstonesc.com/ContactUs/tabid/54/Default.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        data = '------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="__EVENTTARGET"\r\n\r\ndnn:ctr372:CFD:cmdSend\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="__EVENTARGUMENT"\r\n\r\n\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="__VIEWSTATEGENERATOR"\r\n\r\nBBA64215\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:txtEmail"\r\n\r\n$target\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:txtName"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:cfd1"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:cfd2"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:cfd3"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:cfd4"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:cfd5"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:cfd6"\r\n\r\n$text\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="dnn:ctr372:CFD:chkCopy"\r\n\r\non\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="ScrollTop"\r\n\r\n\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="__dnnVariable"\r\n\r\n\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp\r\nContent-Disposition: form-data; name="__VIEWSTATE"\r\n\r\nmr5hn4QHLTD8ee/ehxtdBe1rT141Eb0LfUJgSqP7MbLlvmZAQx4LrRqNhCwRC0Jw0eCwYg5i59gT2LqX5VNZSbo2nyNzWi5XwiYCDiEjh2kL0QYhTaestfIiI/tDfv+MSep7mFQqPchJ6lH+0kcnCqwSQsAIgrGW2BXaeahxRpy6vDo5dL5UBi3qZlbhl8bw5cf1eNBf7Pw8kTFUjjT1fkK1B/6Ee6917ZVKwXMjvm22LqrWlwK2ld6R94u640NzLoxo+M7sI2u9OWNvwq7fB11WtQ4+2fyNk9ByBGKdyFOrEL6t5ujSfs8B/80u22duaPFUsd/JY9x/fB4IDyZqnx5/lcPYxNXbkYu9zm0i0iYPOZ4lDvfjJzOsx24Hv6PU/jnxqKwcdAjQK3wuk5udIy7oMHgfQ4WCyxdVuzZoiTObSzcTZYJRrMeIIVVgHpZqrUCbroOCd5+FRz5VRhAuxTo5YxPk/TS+1l8cDklMRaNrjY0cVMO08nIA5q7zRynnqf4iDHSbzIsK8olZ4faD9/IS2D+8WdjDbRbhjIWwS4jZws039L9zzhA7uw9ITZx9FSNtubDV5ZbcgnCvkAuoL3DMYFryZ6MxOo990aDbfn2vY7haFdFlg1QzuWCoevvQgBc+pAUP9zDbCYzzPbs8E+tiXWqdcz+TYhTowwYJ0MncqdV5/l7ZVVFBzzTF+ePOT6zSdDsvfB8qbmYJwVqDub29R1xq5WwvCQqcdq8iN8gv6rNFdWmw/Zf2OPwvEiJnEUaZ7XoAPIuFKOQ3E/PJYyQ73Uuhag59MzwrVFqamRZfj+Uh0tElpTur2SN2hfi5+HBLnBwCgnLXnakMMW+mfeU3JwG0irxGKRxEOR1mAN15iRPBR5njbuX27cgT/w2vZoiiHw==\r\n------WebKitFormBoundaryEuuJHgQMGPchcHvp--\r\n'
        data = Template(data).substitute({'target': target, 'text': text})

        response = requests.post('http://samsonstonesc.com/ContactUs/tabid/54/Default.aspx', cookies=cookies,
                                 headers=headers, data=data, verify=False, proxies=proxies)
        return response


if __name__ == '__main__':
    success_message = 'Thank you'
    project_name = 'samsonstonesc'
    promo_link = 'bit.ly/3McQq9z'
    spam = ConcreteSpam(promo_link, project_name, success_message, text_encoding='latin-1')
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently(10)
