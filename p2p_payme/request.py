import requests
import json

class PaymeApi:
    def login(self):
        data = {"method": "users.log_in", "params": {"login": "909174227", "password": "AErkinov101"}}
        url = "https://payme.uz/api/users.log_in"
        send_activation_url = "https://payme.uz/api/sessions.get_activation_code"

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        
        resp = requests.post(url, data=json.dumps(data), timeout=20, headers=headers)
        
        api_session = resp.headers.get("API-SESSION")

        headers["API-SESSION"] = api_session
        
        print(resp.headers)

        activation_code = requests.post(send_activation_url, data=json.dumps({"method": "sessions.get_activation_code", "params": {}}), timeout=20, headers=headers)
    

        print(activation_code.text)
    


PaymeApi().login()
