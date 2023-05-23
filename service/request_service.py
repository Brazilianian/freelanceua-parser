import requests


def send_request(method, url):
    return requests.request(
        method=method,
        url=url
    )
