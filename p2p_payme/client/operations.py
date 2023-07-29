from p2p_payme.auth.api import Authenticator
from .scheme import CardList, ChequeList
from .manager import CardManager, ChequeManager
from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Optional


class PaymeClient(Authenticator):
    """
        PaymeClient provides various functions related to Payme, such as get_cards, get_cheques, etc.
        Before using any methods, it will log in every time to obtain a new API key.
    """

    def __init__(self, phone_number: str, password: str, device: str):
        """
            Initialize PaymeClient with user keys and device information
        """
        
        self.phone_number = str(phone_number)
        self.password = password
        self.device = device


    def set_auth_headers(self):
        """
            Set authentication headers and log in to obtain the API key.
        """

        self.auth_headers = {
            "Device": self.device
        }

        super().login(self.phone_number, self.password, self.auth_headers)
        self.auth_headers["API-SESSION"] = self.api_key
    


    # Decorator that calls set_auth_headers to ensure authentication before method execution
    def auth_required(func):
        def wrapper(self, *args, **kwargs):
            self.set_auth_headers()
            return func(self, *args, **kwargs)

        return wrapper


    @property
    @auth_required
    def cards(self):
        """
            Get all cards associated with the user.
        """

        path = "cards.get_all"

        response = self.post(path, {}, self.auth_headers).json()

        # Use response serializer and card serializer
        card = CardList.from_response(response)

        return CardManager(card.cards)

    
    @auth_required
    def transactions(self, card_id: str, from_: Optional[datetime] = None, to: datetime = datetime.now()):
        """
            Get incoming transactions for a specific card.
        """

        path = "cheque.get_all"
        
        # Subtract one month from 'from_' and 'to' to comply with Payme requirements
        to = to - relativedelta(months=1)

        data = {
            "card": [card_id],
            "category": ["589dca36333ec20890b25966", "56e95c616b6e8a6b89845274"],  # get only P2P transactions
            "operation": 1,  # get only P2P transactions
            "count": 24,
            "to": {
                "day": to.day,
                "month": to.month, 
                "year": to.year
            }
        }

        # Set from_ if it is not None

        if from_ is not None:
            from_ = from_ - relativedelta(months=1) 

            data["from"] = {
                "day": from_.day,
                "month": from_.month,
                "year": from_.year
            }

        response = self.post(path, data, self.auth_headers).json()

        # Use response serializer and cheque serializer

        cheque = ChequeList.from_response(response)

        return ChequeManager(cheque.cheques)

    

        
        