from auth.api import Authenticator
from .scheme import CardList, ResponseScheme
from .manager import CardListWrapper

class PaymeClient(Authenticator):
    """
        PaymeClient it has many functions of payme like a get_cards, get_cheques and etc.
        Before using any methods it will login everytime for getting new api_key.
    """

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


    @property
    @auth_required
    def cards(self):
        """
            Get all cards
        """

        path = "cards.get_all"

        response = self.post(path, {}, self.auth_headers).json()

        # Use response serializer and card serializer

        response = ResponseScheme.parse_obj(response)
        card = CardList.parse_obj(response.result)

        return CardListWrapper(card.cards)



        
        