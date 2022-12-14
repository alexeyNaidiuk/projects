import requests

import module


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        cookies = {
            '_ga': 'GA1.2.767868104.1671017237',
            '_gid': 'GA1.2.881482959.1671017237',
            'fpestid': 'iYm4xvbtIMiYMJ82IoG1cVH7ixqmLtTgYOX4-8j2qxxC_Kzn3Uj5CNem35EkhekS0-t5kw',
            '_cc_id': '8656f05083e3529ed2026c39ade9e920',
            'panoramaId_expiry': '1671103638429',
            'laravel_session': 'eyJpdiI6InBqQnIzMzlBcUNuY0JzUGxNcWR0TVE9PSIsInZhbHVlIjoiUzBBRzg0WWdXWTVJOTB0Y21TOVBaZU1qanI2T3NhdGp4QkFWTm1RK3dLdEltNE9maTJGeGxiYVBFT3FSVXJRblFzOENpVW41eWZiT0s3dFFEUitsZmc9PSIsIm1hYyI6IjY4NTlkY2QzNzk5Y2JiNTg0MWU3NjgzMTZhM2VlZDExNjNkMDAzNzQzZTI0YzU1MmJiZWRjYzAwMDg0ZWU1OWUifQ%3D%3D',
            'sc_is_visitor_unique': 'rx10308538.1671017307.8C9D13261F884F7AF5EAA859B484AFD7.1.1.1.1.1.1.1.1.1',
            '_gat': '1',
            'mp_d273ddf4c3dc291ea9819a5d7b55c21a_mixpanel': '%7B%22distinct_id%22%3A%20%2218510638928c63-0d163005d5f426-26021151-1fa400-185106389297a4%22%2C%22%24device_id%22%3A%20%2218510638928c63-0d163005d5f426-26021151-1fa400-185106389297a4%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': '_ga=GA1.2.767868104.1671017237; _gid=GA1.2.881482959.1671017237; fpestid=iYm4xvbtIMiYMJ82IoG1cVH7ixqmLtTgYOX4-8j2qxxC_Kzn3Uj5CNem35EkhekS0-t5kw; _cc_id=8656f05083e3529ed2026c39ade9e920; panoramaId_expiry=1671103638429; laravel_session=eyJpdiI6InBqQnIzMzlBcUNuY0JzUGxNcWR0TVE9PSIsInZhbHVlIjoiUzBBRzg0WWdXWTVJOTB0Y21TOVBaZU1qanI2T3NhdGp4QkFWTm1RK3dLdEltNE9maTJGeGxiYVBFT3FSVXJRblFzOENpVW41eWZiT0s3dFFEUitsZmc9PSIsIm1hYyI6IjY4NTlkY2QzNzk5Y2JiNTg0MWU3NjgzMTZhM2VlZDExNjNkMDAzNzQzZTI0YzU1MmJiZWRjYzAwMDg0ZWU1OWUifQ%3D%3D; sc_is_visitor_unique=rx10308538.1671017307.8C9D13261F884F7AF5EAA859B484AFD7.1.1.1.1.1.1.1.1.1; _gat=1; mp_d273ddf4c3dc291ea9819a5d7b55c21a_mixpanel=%7B%22distinct_id%22%3A%20%2218510638928c63-0d163005d5f426-26021151-1fa400-185106389297a4%22%2C%22%24device_id%22%3A%20%2218510638928c63-0d163005d5f426-26021151-1fa400-185106389297a4%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
            'Origin': 'https://classmill.com',
            'Referer': 'https://classmill.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            '_token': 'bfuLy21W52kNP2FErfZofzNHzS3EodSbYqGUaiA7',
            'firstname': 'testtestest',
            'lastname': 'testtestest',
            'email': 'softumwork+123aawd@gmail.com',
            'password': 'tc12rttZxr3test',
            'signup': '',
        }

        response = requests.post('https://classmill.com/processsignup', cookies=cookies, headers=headers, data=data)

        print(response.text)
        return response


if __name__ == '__main__':
    project_name = 'spam'
    s = ''

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3VyF5El'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        # promo_link=promo_link
    )
    res = spam.send_post()
    # if res:
    #     spam.run_concurrently()
