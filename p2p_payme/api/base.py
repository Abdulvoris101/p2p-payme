import requests
from p2p_payme.config.constants import BASE_URL
import json
from requests.exceptions import ConnectTimeout
import time
import sys

MAX_RETRIES = 3

class APIRequest:
    def __init__(self):
        self.default_headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        self.url = BASE_URL

    def request(self, path: str, method: str, data={}, headers={}, retries=0):
        self.default_headers.update(headers)
        self.url = self.url + path
        
        try:

            response = requests.request(
                method=method,
                url=self.url,
                data=json.dumps(data),
                headers=self.default_headers,
                timeout=20
            )

            return response
        
        except ConnectTimeout as e:
            # Retry the request up to MAX_RETRIES times if ConnectTimeoutError occurs

            if retries < MAX_RETRIES:
                print(f"ConnectTimeoutError occurred. Retrying ({retries+1}/{MAX_RETRIES})...")
                time.sleep(3)
                return self.request(path, method, data, headers, retries=retries+1)

            else:
                print(f"ConnectTimeoutError: Maximum number of retries reached.")
                raise  # Raise the exception to be handled at a higher level
            
        except Exception as e:
            print(e)
            sys.exit(1)
    
    @classmethod
    def post(cls, path: str, data={}, headers={}):
        instance = APIRequest()

        data = {
            "method": path,
            "params": data
        }

        try:
            response = instance.request(
                path=path,
                method="POST",
                data=data,
                headers=headers
            )

            error = response.json().get("error")


            if response is None:
                raise Exception("API response is None. Please check the request.")

            elif error is not None:

                if error.get("code") == -32602:
                    raise Exception("Invalid code!")

                raise Exception(error.get("message"))
            
            return response


        except AttributeError as e:
            raise Exception("API response is not JSON. Please check the request.")
        
        except Exception as e:
            print(e)
            sys.exit(1)

    @classmethod
    def get(cls, path: str, headers={}):
        instance = APIRequest()

        return instance.request(
            path=path,
            method="GET",
            headers=headers
        )

    
