import datetime

from bs4 import BeautifulSoup
from service.request_service import send_request

url = "https://freelance.ua/orders"
# TODO add filters
params = []
features = 'html.parser'


def get_beautiful_soap():
    response = send_request('GET', url)
    print(f"{datetime.datetime.now()}: Sent http request to {url}")
    return BeautifulSoup(response.content, features)
