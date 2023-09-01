import requests
from selenium import webdriver

from logger_configuration import logger


def send_http_request(method,
                      url,
                      session,
                      headers=None):
    response = session.request(
        method=method,
        url=url,
        headers=headers
    )

    match response.status_code:
        case 200:
            logger.info(f"Response 200 from {url}")
        case 500:
            logger.warning(f"Response 500 from {url}")
            response.content = []

    return response


def create_session():
    return requests.Session()


def init_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(options)


browser = init_chrome_driver()


def send_request_through_webdriver(url):
    try:
        browser.get(url)
        logger.info(f"Response 200 from {url}")
        return browser.page_source
    except ConnectionError as e:
        logger.warning(f"Response 500 from {url}: {str(e)}")
        return ""
