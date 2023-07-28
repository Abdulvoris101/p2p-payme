from auth.api import Authenticator
from .scheme import CardList, ResponseScheme, ChequeList
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

    
    @auth_required
    def transactions(self, card_id):
        """
            Get incoming transactions
        """

        path = "cheque.get_all"

        data = {
            "card": [card_id],
            "category": ["589dca36333ec20890b25966", "56e95c616b6e8a6b89845274"],  # gets only p2p transactions
            "operation": 1,  # gets only incoming cheques
        }

        response = self.post(path, data, self.auth_headers).json()

        # Use response serializer and cheque serializer

        response = ResponseScheme.parse_obj(response)
        cheque = ChequeList.parse_obj(response.result)

        return cheque.cheques


        
        