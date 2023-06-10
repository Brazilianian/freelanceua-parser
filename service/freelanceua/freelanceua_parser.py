from bs4 import BeautifulSoup

from service import request_service

url = "https://freelance.ua/orders"
params = []
features = 'html.parser'

session = request_service.create_session()


def get_beautiful_soap():
    response = request_service.send_http_request('GET', url, session)
    return BeautifulSoup(response.content, features)
