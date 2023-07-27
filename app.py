from client import PaymeClient
import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.environ.get("API_KEY")
DEVICE = os.environ.get("DEVICE")

client = PaymeClient(API_KEY, DEVICE)

client.get_cards()