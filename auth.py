from auth import Authenticator
import os
from dotenv import load_dotenv
import time

load_dotenv()

auth = Authenticator()

phone_number = os.environ.get("PHONE_NUMBER")
password = os.environ.get("PASSWORD")

auth.set_credentials(phone_number, password)

verification_code = input("Verif code: ")

device = auth.activate(verification_code)

time.sleep(3)
data = auth.login_with_device(device)

print(data)

# This is for testing functionality of code.