import requests

from module.spam_abstraction import Spam

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Origin': 'http://www.laveleholidays.com',
    'Referer': 'http://www.laveleholidays.com/booking-form/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


class ConcreteSpam(Spam):

    def post(self, target) -> requests.Response:
        data = {
            'fullName': self.get_text(),
            'Telephone': self.get_text(),
            'Email': target,
            'CheckInDate': '1111-11-11',
            'CheckOutDate': '1111-11-11',
            'NoOfGuests': '1',
            'sendCopy': '1',
            'bookingform': 'Submit',
        }

        response = requests.post('http://www.laveleholidays.com/email_send.php', headers=headers, data=data,
                                 proxies=self.get_proxies())
        return response


if __name__ == '__main__':
    success_message = 'Your booking request has been sent '
    project_name = 'laveleholidays'
    promo_link = 'bit.ly/3TPCPaM'
    spam = ConcreteSpam(promo_link, project_name, success_message)
    res = spam.send_post()
    if res:
        spam.run_concurrently(5)
