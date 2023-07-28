from api.base import APIRequest
from config import constants

class Authenticator(APIRequest):
    def __init__(self):
        super().__init__()
    
    def login(self, login, password, headers={}):
        """Logs in the user with the provided credentials."""

        path = "users.log_in"

        credentials = {
            "login": login,
            "password": password
        }

        response = self.post(path, credentials, headers)

        # Set api_key 
        self.api_key = response.headers.get("API-SESSION")


    def set_credentials(self, login, password):
        """
        Sets the user's login credentials and calls the login method. And calls send verification method.

        """

        self.phone_number = login # Define with self var to access via other methods
        self.password = password 


        # Call login and send_activation methods

        self.login(login, password)
        self.send_activation_code()



    def send_activation_code(self):

        """Sends activation code to users's phone number"""

        path = "sessions.get_activation_code"

        self.auth_headers = {
            "API-SESSION": self.api_key
        }

        # Send activation code to phone

        self.post(path, {}, self.auth_headers) 



    def activate(self, verification_code):
        """ 
            Activate account via verification code.
        """

        path = "sessions.activate"

        data = {
            "code": verification_code, 
            "device": True  # set true to setup device
        }

        # Activate via verification code.
        self.post(path, data, self.auth_headers)
        
        # Register device
        device = self.register_device() # get device
        
        return device
    
    
    def register_device(self):
        """
            Registers device and returns entered device 

            This method sends a request to the 'devices.register' endpoint to register the user's device
            and obtain the 'device_data'. The device name is obtained from the 'constants' module.
        """

        path = "devices.register"
        
        data = {
            "display": constants.DEVICE_NAME,
            "type": 2
        }

        # Request to register device
        response = self.post(path, data, self.auth_headers).json()
        
        result = response.get("result")

        device_id = result.get("_id")
        device_key = result.get("key")

        # Combine device_id and device_key to get device
        device = f"{device_id}; {device_key};"

        return device


