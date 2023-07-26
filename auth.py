from auth.client import Authenticator

auth = Authenticator()

auth.set_credentials("YOUR_PHONE", "YOUR_PASSWORD")

verification_code = input("Verif code: ")

deviceId = auth.activate(verification_code)


# This is for testing functionality of code.