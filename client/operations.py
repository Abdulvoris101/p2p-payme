from auth.api import Authenticator

class PaymeClient(Authenticator):
    def __init__(self, api_key, device):
        """
            Set user keys and devices
        """

        self.api_key = api_key
        self.device = device

        self.set_auth_headers()


    def set_auth_headers(self):
        self.auth_headers = {
            "Device": self.device,
            "API-SESSION": self.api_key
        }


    def get_cards(self):
        """
            Get all cards
        """

        path = "cards.get_all"

        cards = self.post(path, {}, self.auth_headers)
        

        
        