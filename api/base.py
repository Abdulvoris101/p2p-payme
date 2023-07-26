import requests
from config.constants import BASE_URL
import json

class APIRequest:
    def __init__(self):
        self.default_headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        self.url = BASE_URL

    def request(self, path, method, data={}, headers={}):
        self.default_headers.update(headers)
        self.url = self.url + path
        
        response = requests.request(
            method=method,
            url=self.url,
            data=json.dumps(data),
            headers=self.default_headers,
            timeout=20
        )

        return response
    
    @classmethod
    def post(cls, path, data={}, headers={}):
        instance = cls()

        data = {
            "method": path,
            "params": data
        }

        return instance.request(
            path=path,
            method="POST",
            data=data,
            headers=headers
        )

    @classmethod
    def get(cls, path, headers={}):
        instance = cls()

        return instance.request(
            path=path,
            method="GET",
            headers=headers
        )

    
