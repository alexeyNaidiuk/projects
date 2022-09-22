from itertools import cycle
from time import sleep

from seleniumwire.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

manager = ChromeDriverManager().install()
driver = Chrome(manager)


def retrieve_posts():
    posts = []
    for request in driver.requests:
        if b'softum' in request.body:
            request_dict = {'url': request.url, 'headers': dict(request.headers), 'data': request.body}
            posts.append(request_dict)
    return posts
