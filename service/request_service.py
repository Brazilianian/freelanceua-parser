import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def send_http_request(method,
                      url,
                      session,
                      headers=None):
    response = session.request(
        method=method,
        url=url,
        headers=headers
    )
    print(response)
    return response


def create_session():
    return requests.Session()


def init_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


browser = init_chrome_driver()


def send_request_through_webdriver(url):
    browser.get(url)
    return browser.page_source
