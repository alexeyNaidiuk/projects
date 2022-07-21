from zipfile import ZipFile

from faker import Faker
from seleniumwire.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from data import get_proxies, generate_proxy

all_proxies = get_proxies(r'C:\Users\Admin\Desktop\projects\west_proxy.txt')
proxy_generator = generate_proxy(all_proxies)
DRIVER_MANAGER = ChromeDriverManager().install()


def get_proxy_file_extension(proxy: str):
    user, password, host, port = [b for a in proxy.split('@') for b in a.split(':')]
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (host, port, user, password)
    plugin_filename = 'proxy_auth_plugin.zip'

    with ZipFile(plugin_filename, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    return plugin_filename


def try_with_browser():
    proxy = next(proxy_generator).replace('http://', '')
    proxy_file_extension = get_proxy_file_extension(proxy)
    options = ChromeOptions()
    options.add_argument(f'--user-agent={Faker().chrome()}')
    options.add_argument(r'--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default')
    options.add_argument(r'--profile-directory=Default')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_extension(proxy_file_extension)
    driver = Chrome(DRIVER_MANAGER, options=options, seleniumwire_options={'verify_ssl': False})
    driver.get('https://www.wm.com/ca/en/support/customer-support/contact-us-form')
    with open(r'C:\Users\Admin\AppData\Roaming\JetBrains\PyCharm2022.1\scratches\scratch.js') as file:
        script = file.read()
    driver.execute_script(script)
    breakpoint()


if __name__ == '__main__':
    try_with_browser()
