from bs4 import BeautifulSoup

from service import request_service

url = "https://freelancehunt.com/ua/projects"
params = []
features = 'html.parser'


def get_beautiful_soap():
    html = request_service.send_request_through_webdriver(url)
    return BeautifulSoup(html, features)
