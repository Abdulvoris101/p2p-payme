from api.base import APIRequest
from config import constants

class Authenticator(APIRequest):
    def __init__(self):
        super().__init__()
    
    def login(self, login, password, headers={}):
        """Logs in the user with the provided credentials."""

        path = "users.log_in"

        credentials = {"login": login, "password": password}
        
        self.login_data = self.post(path, credentials, headers)
        self.api_key = self.login_data.headers.get("API-SESSION")
        
    
    def set_credentials(self, login, password):
        """
        Sets the user's login credentials and calls the login method. And calls send verification method.

        """

        self.login(login, password)
        self.send_activation_code()


    def send_activation_code(self):

        """Sends activation code to users's phone number"""

        path = "sessions.get_activation_code"

        self.auth_headers = {
            "API-SESSION": self.api_key
        }

        data = self.post(path, {}, self.auth_headers)

    def activate(self, verification_code):
        """ 
            Activates user's account via verification code
        """

        path = "sessions.activate"

        data = {
            "code": verification_code, 
            "device": True
        }

        self.activation_data = self.post(path, data, self.auth_headers)

        # Automaticaly register device and returns deviceId and api-key

        return {
            "device-id": self.register_device(),
            "api-key": self.api_key
        }
    

    def register_device(self):
        """
            Registers device and returns entered device_id 

            This method sends a request to the 'devices.register' endpoint to register the user's device
            and obtain the 'device_data'. The device name is obtained from the 'constants' module.
        """

        path = "devices.register"
        
        data = {
            "display": constants.DEVICE_NAME,
            "type": 2
        }

        self.device_data = self.post(path, data, self.auth_headers)

        return self.device_data.json().get("result").get("_id")







