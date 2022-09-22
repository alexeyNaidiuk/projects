from pathlib import Path
from time import time
import logging
from concurrent.futures import ThreadPoolExecutor
from time import sleep

import requests

from module.data import get_turk_spinned_text, TurkeyTargetPool, WwmixProxyPool, ProjectController, Pool

PROM_LINK = 'shortin.us/Cae12'
PROJECT_NAME = Path(__file__).name.replace('.py', '')
target_pool: Pool = TurkeyTargetPool()
PROXY_POOL: Pool = WwmixProxyPool()
project: ProjectController = ProjectController(PROJECT_NAME, PROM_LINK)
use_proxy: bool = False
logger = logging.getLogger(PROJECT_NAME)
logging.basicConfig(format='%(asctime)s: %(message)s')
logger.setLevel(logging.INFO)


def post(target: str, text: str, proxies: dict | None = None) -> requests.Response:
    cookies = {
        'OptanonAlertBoxClosed': '2022-09-20T09:13:58.994Z',
        '_gid': 'GA1.3.1177022256.1663665239',
        '_scid': 'afb21345-06ed-4830-b74d-cdd5080ba514',
        '_fbp': 'fb.2.1663665239421.1790363392',
        '_gcl_au': '1.1.168186005.1663665239',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample': '1',
        '_hjSession_1430839': 'eyJpZCI6IjgwNzEwMjU4LTU1OWUtNGNkOC1hMDg1LWEwOWRjYWYxMjY0NiIsImNyZWF0ZWQiOjE2NjM2NjUyMzk2NTksImluU2FtcGxlIjp0cnVlfQ==',
        '_hjIncludedInPageviewSample': '1',
        '_hjAbsoluteSessionInProgress': '0',
        '_clck': '1t8fbsw|1|f51|0',
        '_hjSessionUser_1430839': 'eyJpZCI6ImU1ZGIxMmNlLWYyNTAtNWQ0Ni05MmExLWYxNDI5MGRiNjg4MCIsImNyZWF0ZWQiOjE2NjM2NjUyMzk2MjEsImV4aXN0aW5nIjp0cnVlfQ==',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Sep+20+2022+12%3A14%3A50+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.31.0&isIABGlobal=false&hosts=&consentId=00a3c761-eb80-46a1-b86f-efedfd9d0b50&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=DE%3BHE&AwaitingReconsent=false',
        '_ga': 'GA1.3.576011205.1663665239',
        '_uetsid': '8fb4d7c038c411ed87976b45b740b0ee',
        '_uetvid': '8fb4fff038c411ed9bfd5d642b6dafc8',
        '_clsk': '1crgdpk|1663665292137|3|1|l.clarity.ms/collect',
        '_ga_PK12YLCPD2': 'GS1.1.1663665239.1.1.1663665293.0.0.0',
    }
    headers = {
        'authority': 'www.amnesty.org.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'origin': 'null',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    data = {
        'personal_details[title]': '2322',
        'personal_details[firstname]': 'test',
        'personal_details[lastname]': 'test',
        'personal_details[email]': target,
        'personal_details[opt_in_visibility]': '',
        'personal_details[over_18]': 'Y',
        'personal_details[dob][day]': '',
        'personal_details[dob][month]': '',
        'personal_details[dob][year]': '',
        'personal_details[dob_visibility]': '',
        'phone_number': 'test',
        'please_tell_us_what_kind_of_feedback_you_are_submitting': 'Comment',
        'please_tell_us_what_your_feedback_is_about': 'Other',
        'message': text,
        'would_you_like_a_response': 'Yes',
        'op': 'Send message',
        'form_build_id': 'form-fusmpAoj0R9dd9O3Vy0JoB-46CVYkffm80jeTNJ0auU',
        'form_id': 'webform_submission_submit_feedback_paragraph_2118_add_form',
    }
    response = requests.post(
        'https://www.amnesty.org.uk/send-us-feedback', cookies=cookies, headers=headers, data=data, proxies=proxies
    )
    logger.info(response)
    return response


def try_to_post(text, target) -> bool:
    content = None
    while not content:
        if use_proxy:
            proxy = next(PROXY_POOL)
            proxy = {'http': proxy, 'https': proxy}
        else:
            proxy = None
        try:
            response = post(text=text, target=target, proxies=proxy)
            content = response.content.decode()
        except Exception as e:
            logger.error(e)
    return 'Thank you for getting in touch.' in content


def main(target='softumwork@gmail.com'):
    if not project.status():
        logger.debug('sleeping')
        sleep(120)
        return False
    target: str = target.encode().decode('latin-1')
    text: str = get_turk_spinned_text(PROM_LINK, with_stickers=True, decoded=False)
    result: bool = try_to_post(text=text, target=target)
    if result:
        logger.info(f'{result} {target}')
        project.send_good_status()
        project.send_count(1)
    else:
        logger.error(result)
        project.send_bad_status()


def threaded_main():
    with ThreadPoolExecutor(50) as executor:
        executor.map(main, [target for target in target_pool])


if __name__ == '__main__':
    main()
