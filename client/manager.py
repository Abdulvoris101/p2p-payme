from .scheme import Card, Cheque
from typing import List


def handle_exception(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        
        except Exception as e:
            # Handle the exception here (e.g., log, notify, etc.)
            print(f"Exception occurred: {e}")

            return None

    return wrapper


class CardManager:
    def __init__(self, cards: List[Card]):
        """
            ChequeManager handles a list of Cheque objects.

        """

        self._cards = cards
    

    def _filter_objects(self, **kwargs):
        """
            Filter cheques based on provided attributes (keyword arguments).

        """
        filtered_objects = self._cards

        for key, value in kwargs.items():
            filtered_objects = [card for card in filtered_objects if getattr(card, key) == value]

        return filtered_objects

    @handle_exception
    def filter(self, **kwargs):
        """
            Filter cards based on provided attributes (keyword arguments).
        """
        filtered_cards = self._filter_objects(**kwargs)

        return CardManager(filtered_cards)
    
    @handle_exception
    def get(self, **kwargs):
        """
          Get card by attribute
        """
        
        filtered_cards = self._filter_objects(**kwargs)

        if len(filtered_cards) != 1:
            return None
        
        return filtered_cards[0]
        
    @handle_exception
    def first(self):
        """
            Get the first card from the list.
        """
        if self._cards:
            return self._cards[0]
            
        return None

    def all(self):
        """
            Get all cards from the list.
        """
    
        return self._cards


class ChequeManager:
    def __init__(self, _cheques: List[Cheque]):
        self._cheques = _cheques
    
    @handle_exception
    def filter(self, **kwargs):
        filter_transactions = self._cheques

        for key, value in kwargs.items():
            
            filter_transactions = [cheque for cheque in filter_transactions if getattr(cheque, key) == value]

        return filter_transactions
    
    @handle_exception
    def all(self):
        """
            Get all cheque from the list.
        """
        return self._cheques

    @handle_exception
    def first(self):
        """
            Get the first cheque from the list.
        """
        if self._cheques:
            return self._cheques[0]
            
        return None


