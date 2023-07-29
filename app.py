from client import PaymeClient
import os
import dotenv
from datetime import datetime, timedelta

dotenv.load_dotenv()


PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
PASSWORD = os.environ.get("PASSWORD")
DEVICE = os.environ.get("DEVICE")
from_ = datetime.now() - timedelta(days=30)

client = PaymeClient(PHONE_NUMBER, PASSWORD, DEVICE)

card = client.cards.get(name="uzcard")

transactions = client.transactions(card.id, from_=from_).all()


for transaction in transactions:
    data = {
        "create_time": transaction.create_time,
        "amount": transaction.amount / 100,
        "description": transaction.description
    }

    print(data)
