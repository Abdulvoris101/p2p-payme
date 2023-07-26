from api.base import APIRequest

class Authenticator(APIRequest):
    def __init__(self):
        super().__init__(self)
    

    def login(self, username, password):
        path = "/users.log_in"
        credentials = {"username": username, "password": password}
        
        self.post(path, credentials)

