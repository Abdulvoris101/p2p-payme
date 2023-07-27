from auth.client import Authenticator

class PaymeClient(Authenticator):
    def __init__(self, phone_number, password, device_id):
        """
            Set user credentials
        """
        self.phone_number = phone_number
        self.password = password
        self.device_id = device_id

    def get_device_api_session(self):
        self.device_auth_headers = {
            "Device": self.device_id
        }

        self.api_session = self.login(self.phone_number, self.password, self.device_auth_headers)
        self.device_auth_headers["API-SESSION"] = self.api_session

    def get_cards(self):
        """
            Get all cards
        """

        path = "cards.get_all"

        self.get_device_api_session()

        cards = self.post(path, {}, self.device_auth_headers)

        print(cards.text)


        
        