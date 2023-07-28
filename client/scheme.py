from datetime import date
from pydantic_collections import BaseCollectionModel

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


class CardList(BaseCollectionModel[Card]):
    pass