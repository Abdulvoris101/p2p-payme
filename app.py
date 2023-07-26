from auth.client import Authenticator


auth = Authenticator()

auth.set_credentials("YOUR_USERNAME", "YOUR_PASSWORD")

verification_code = input("Verif code: ")

deviceId = auth.activate(verification_code)
