from .scheme import Card
from typing import List


class CardListWrapper:
    def __init__(self, cards: List[Card]):
        self._cards = cards
    
    def filter_cards(self, **kwargs):
        filtered_cards = self._cards

        for key, value in kwargs.items():
            filtered_cards = [card for card in filtered_cards if getattr(card, key) == value]

        return filtered_cards

    def filter(self, **kwargs):
        """
        Filter cards based on provided attributes (keyword arguments).
        """
        filtered_cards = self.filter_cards(**kwargs)

        return CardListWrapper(filtered_cards)


    def get(self, **kwargs):
        """
          Get card based on provided attributes (keyword arguments).
        """
        filtered_cards = self.filter_cards(**kwargs)

        if len(filtered_cards) > 1 or filtered_cards is None:
            return None
        
        return filtered_cards[0]
        

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

