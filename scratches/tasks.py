import logging
import webbrowser

from invoke import task
import requests


def read(filename) -> list:
    with open(filename) as file:
        return file.read().splitlines()


def save(line) -> None:
    with open('parsed.txt', 'a') as file:
        file.write(line + '\n')


def is_recaptcha_represented_on_site(resp) -> bool:
    res = 'recaptcha' in resp.content.decode('latin-1')
    return res


@task
def sniff_donnors(c):
    lines = read('jformcontact_email_copydepthall.txt')
    parsed = read('parsed.txt')
    lines = set(lines) - set(parsed)
    lines = iter(lines)

    while True:
        for _ in range(20):
            line = next(lines)
            try:
                resp = requests.get(line, timeout=5)
            except Exception as error:
                logging.exception(error)
                continue
            save(line)
            if not is_recaptcha_represented_on_site(resp):
                webbrowser.open(line)
        breakpoint()
