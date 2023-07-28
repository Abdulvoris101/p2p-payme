from auth.api import Authenticator
from .scheme import CardList

class PaymeClient(Authenticator):
    def __init__(self, phone_number, password, device):
        """
            Set user keys and devices
        """

        self.phone_number = phone_number
        self.password = password
        self.device = device


    def set_auth_headers(self):
        self.auth_headers = {
            "Device": self.device
        }
        super().login(self.phone_number, self.password, self.auth_headers)
        self.auth_headers["API-SESSION"] = self.api_key
    


    # Decorator which is call set_auth_headers
    def auth_required(func):
        def wrapper(self, *args, **kwargs):
            self.set_auth_headers()
            return func(self, *args, **kwargs)

        return wrapper


    @auth_required
    def get_cards(self):
        """
            Get all cards
        """

        path = "cards.get_all"

        response = self.post(path, {}, self.auth_headers).json()

        # Use card serializer 

        cards = CardList(response.get("result"))

        return cards



        
        