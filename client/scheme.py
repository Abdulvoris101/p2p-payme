from datetime import date
from pydantic_collections import BaseCollectionModel
from typing import List
from pydantic import BaseModel, Field



# Model to represent a currency.
class Currency(BaseModel):
    numeric_code: int
    alpha_code: str
    title: str

# Model to represent a vendor.
class Vendor(BaseModel):
    name: str
    processing: str
    processing_id: str


# Model to represent a card.
class Card(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    number: str
    expire: str
    owner: str
    main: bool
    active: bool
    balance: int
    currency: int
    
    currency_details: Currency
    vendor_info: Vendor

    date: int

    @classmethod
    def from_response(cls, response: dict) -> 'Card':
        return cls.parse_obj(response.get('result'))


class CardList(BaseModel):
    cards: List[Card]

    @classmethod
    def from_response(cls, response: dict) -> 'Cheque':
        return cls.parse_obj(response.get('result'))

class Cheque(BaseModel):
    id: str = Field(..., alias="_id")
    create_time: int
    pay_time: int
    cancel_time: int
    type: int
    description: str
    card: dict
    amount: int
    currency: int

    @classmethod
    def from_response(cls, response: dict) -> 'Cheque':
        return cls.parse_obj(response.get('result'))
    


class ChequeList(BaseModel):
    cheques: List[Cheque]

    @classmethod
    def from_response(cls, response: dict) -> 'Cheque':
        return cls.parse_obj(response.get('result'))