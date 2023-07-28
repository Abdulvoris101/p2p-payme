from client import PaymeClient
import os
import dotenv

dotenv.load_dotenv()

PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
PASSWORD = os.environ.get("PASSWORD")
DEVICE = os.environ.get("DEVICE")

client = PaymeClient(PHONE_NUMBER, PASSWORD, DEVICE)

card = client.cards.get(name="uzcard")
transactions = client.transactions(card.id)

print(transactions)