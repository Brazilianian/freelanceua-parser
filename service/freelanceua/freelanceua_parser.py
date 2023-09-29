from bs4 import BeautifulSoup

from service import request_service

url = "https://freelance.ua/orders"
params = []
features = 'html.parser'

session = request_service.create_session()


def get_soap_of_proposals():
    response = request_service.send_http_request('GET', url, session)
    return BeautifulSoup(response.content, features)


def get_soap_of_subcategories(proposal_link: str):
    response = request_service.send_http_request('GET', proposal_link, session)
    return BeautifulSoup(response.content, features)
