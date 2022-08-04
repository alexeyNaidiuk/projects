import requests

from module.data import target_generator, try_to
import spintax

TEXT = '🔥 {Получи|Забери|Используй} 50 {фриспинов|FS|freespins|free spins|spins} за {Регистрацию в клубе|Вход в клуб|Вход в проект|принятие участия в|игру в} Slottica {переходя|перейдя|} по {следующей|этой} ссылке {ниже|} {-|:|} https://bit.ly/3zWpxSO {Поспеши|Поторопись|Торопись|Не задерживайся}, время действия {бонуса|приза|подарка} {ограничено|лимитировано}!'


@try_to
def post(target: str):
    url = 'https://my.flipdish.com/feedmefast/contact'
    headers = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    text = spintax.spin(TEXT)
    data = {
        'Name': text * 4,
        'Phone': text * 100,
        'Email': target,
        'Captcha': '4',
        'message': text,
        'X-Requested-With': 'XMLHttpRequest'
    }

    res = requests.post(url, data, headers=headers)
    return res


def spam(target='softumwork@gmail.com'):
    res = None
    while res is None:
        res = post(target)
    return res, target


if __name__ == '__main__':
    test = spam()
    print(test)
    for target in target_generator(r'C:\Users\Admin\Desktop\projects\targets\alotof.csv'):
        print(spam(target))
