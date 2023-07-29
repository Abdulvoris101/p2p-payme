# p2p-payme package

[![\Telegram\] abdulvoris](https://img.shields.io/badge/Telegram-blue.svg?logo=telegram)](https://t.me/aerkinov1)

## Introduction

p2p_payme is a Python package that provides a simple and convenient way to interact with the Payme API for peer-to-peer (P2P) automation. This package allows users to authenticate, perform various P2P transactions, manage cards, and access transaction history.


## Installation

```
pip install p2p-payme
```

## Authentication
Before using the p2p_payme package, developers need to authenticate to obtain the device_id, which is required for all subsequent interactions with the Payme API. The device_id uniquely identifies the device from which the API requests are being made.

Just write this in the terminal:
```
auth
```

To authenticate, the user needs to run the auth command in the terminal. The user will be prompted to enter their Payme account credentials, including the phone number and password. The provided credentials will be used to log in to the Payme API. 

Upon successful authentication, the device_id will be obtained, and the user will be ready to use the PaymeClient to perform various operations.

## PaymeClient Operations

After obtaining the device_id, you can create an instance of PaymeClient by passing the phone number, password, and device_id. The PaymeClient class provides various methods to interact with the Payme API.

For example, you can use the cards property to retrieve all cards associated with the your's account. Each card object contains details such as card name, number, balance, and currency.

Additionally, the transactions method allows you to retrieve incoming transactions for a specific card. By providing the card ID, developers can obtain details of recent transactions, including transaction ID, amount, and description.

## Cards

`cards`

This property returns all cards associated with the user's account.
```
cards = client.cards.all()
```

`cards.filter(**kwargs)`

This method allows filtering cards based on provided attributes (keyword arguments). You can filter cards by card name, number, balance, currency, etc.

```
# Filter cards by card name
filtered_cards = client.cards.filter(name="My Card")
```

## Transactions (Cheques)

`transactions(card_id: str, from_: Optional[datetime] = None, to: datetime = datetime.now())`

This method retrieves incoming transactions for a specific card. You need to provide the card ID for which you want to get transactions. Optionally, you can specify the time range for the transactions using the `from_` and `to` parameters.

Get transactions for a specific card (replace 'card_id' with the actual card ID)
```
card_id = client.cards.first()
transactions = client.transactions(card_id)
```

## Filtering Cards

The `cards.filter()` method allows you to filter cards based on specific attributes. Here are some of the attributes (keyword arguments) that you can use for filtering:

- `name`: Filter cards by their name.
- `number`: Filter cards by their number.
- `balance`: Filter cards by their balance amount.
- `currency`: Filter cards by their currency type.
- `owner`: Filter cards by the owner's name.

You can pass these attributes as keyword arguments to the `cards.filter()` method. For example:
```
# Filter cards by card name and currency
filtered_cards = client.cards.filter(name="My Card", currency="UZS")
```
You can use one or multiple attributes to filter the cards as per your requirements.

## Example
Here's an example that demonstrates how to use some of the methods available in `PaymeClient`:
```
# Import the PaymeClient class and other required modules
from p2p_payme.client.operations import PaymeClient
from datetime import datetime

# Replace with your Payme account credentials and device information
phone_number = "YOUR_PHONE_NUMBER"
password = "YOUR_PASSWORD"
device = "YOUR_DEVICE_INFORMATION"

# Create a PaymeClient instance with authenticated credentials
client = PaymeClient(phone_number, password, device)


# Get all cards associated with the user's account
cards = client.cards.all()

# Print card details
for card in cards:
    print(f"Card Name: {card.name}")
    print(f"Card Number: {card.number}")
    print(f"Balance: {card.balance}")
    print("-------")

# Get specific card using get
card = client.cards.get(name="uzcard")

# Get transactions for a specific card (replace 'card_id' with the actual card ID)
card_id = "YOUR_CARD_ID"
transactions = client.transactions(card_id)

# Print transaction details
for transaction in transactions:
    print(f"Transaction ID: {transaction.id}")
    print(f"Amount: {transaction.amount}")
    print(f"Description: {transaction.description}")
    print("-------")

# Filter cards by card name and currency
filtered_cards = client.cards.filter(name="My Card", currency="UZS")

# Print filtered card details
for card in filtered_cards:
    print(f"Card Name: {card.name}")
    print(f"Card Number: {card.number}")
    print(f"Balance: {card.balance}")
    print("-------")
```

