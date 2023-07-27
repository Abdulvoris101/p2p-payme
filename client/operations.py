from auth.client import Authenticator

class PaymeClient(Authenticator):
    def __init__(self, api_key, device_id):
        """
            Set user credentials
        """
        self.device_id = device_id
        self.api_key = api_key

    def set_auth_headers(self):
        self.device_auth_headers = {
            "Device": self.device_id,
            "API-SESSION": self.api_key
        }

    def get_cards(self):
        """
            Get all cards
        """

        path = "cards.get_all"

        self.set_auth_headers()

        cards = self.post(path, {}, self.device_auth_headers)

        print(cards.text)


        
        