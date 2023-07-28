from client import PaymeClient
import os
import dotenv

dotenv.load_dotenv()

PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
PASSWORD = os.environ.get("PASSWORD")
DEVICE = os.environ.get("DEVICE")

client = PaymeClient(PHONE_NUMBER, PASSWORD, DEVICE)

# client.get_cards()
print(client.cards.get(id="6243fd35fe5217f5079a3d97"))
