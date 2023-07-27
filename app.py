from client import PaymeClient
import os
import dotenv

dotenv.load_dotenv()

client = PaymeClient(os.environ.get("PHONE_NUMBER"), os.environ.get("PASSWORD"), os.environ.get("DEVICEID"))

client.get_cards()