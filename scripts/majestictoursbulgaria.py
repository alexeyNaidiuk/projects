import requests

import module

URL = 'https://www.majestictoursbulgaria.com/contact_us'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie': 'majestictoursbulgaria_session=eyJpdiI6IkhxTDRPUm5UN0VyMlhFbzV6ZGllMUE9PSIsInZhbHVlIjoiXC9GZmoxbUtKRStUZk1zRVNpS1ZNZVk5REVVc28zQzZ1Vys4d1BZV0c2andZUURYd1FBTXBWelg4eVJsbDNkSTEiLCJtYWMiOiJiNWM4NjczNTNhMWRkNjQzYzhmZmY0NTAyNTNkMTlhNDJlYWMwNDk0YTVhNjY0MjcyYTEzMTY1YjNhYzQ1ZTViIn0%3D'
}


class ConcreteSpam(module.Spam):

    def post(self, target) -> requests.Response:
        text = self.get_text()
        data = {
            '_token': 'IdUXFFT8c4aurkVznouGmAB5KIvGmTbomdkQnUVi',
            'name': text,
            'email': target,
            'phone': target,
            'message': target,
            'copy': 'on',
        }

        response = requests.post(URL, headers=headers, data=data)
        return response


if __name__ == '__main__':
    project_name = 'majestictoursbulgaria'
    s = 'Thank you for contacting us! We will keep in touch.'

    project = 'supercat'  # supercat luckybird allright fortuneclock
    promo_link = 'bit.ly/3BvetfN'
    spam = ConcreteSpam(
        project_name, s,
        referal_project_name=project,
        promo_link=promo_link
    )
    res = spam.send_post()
    if res:
        spam.run_concurrently()
