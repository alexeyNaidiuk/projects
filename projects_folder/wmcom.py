from faker import Faker
from seleniumwire.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from projects_folder.module.data import get_proxies, generate_proxy, get_proxy_file_extension

all_proxies = get_proxies(r'C:\Users\Admin\Desktop\projects\west_proxy.txt')
proxy_generator = generate_proxy(all_proxies)
DRIVER_MANAGER = ChromeDriverManager().install()





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
