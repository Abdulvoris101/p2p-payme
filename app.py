from client import PaymeClient
import os
import dotenv

dotenv.load_dotenv()

client = PaymeClient(os.environ.get("API_SESSION"), os.environ.get("DEVICE"))

client.get_cards()