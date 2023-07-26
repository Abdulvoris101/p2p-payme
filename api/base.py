import requests
from config.constants import BASE_URL


class BaseAPI:
    def __init__(self):
        self.default_headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        self.request_url = BASE_URL

    def request(self, url, method, data={}, headers={}):
        self.default_headers.update(headers)
        self.request_url = self.request_url + url

        response = requests.request(
            method=method,
            url=self.request_url,
            data=data,
            headers=self.default_headers
        )

        return response
    
    def post(self, url, data={}, headers={}):
        self.request(
            url=url,
            method="POST",
            data=data,
            headers=headers
        )

    def get(self, url, headers={}):
        self.request(
            url=url,
            method="GET",
            headers=headers
        )

    
