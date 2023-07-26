from auth.client import Authenticator


auth = Authenticator()

auth.set_credentials("909174227", "AErkinov101")

verification_code = input("Verif code: ")

deviceId = auth.activate(verification_code)
