class AccountClient:
    def __init__(self, client):
        self.client = client

    def build_signup_payload(self, email, password, username, first_name, last_name):
        return {
            "email": email,
            "password": password,
            "username": username,
            "first_name": first_name,
            "last_name": last_name
        }

    def signup_request(self, payload):
        return self.client.post("/api/users/", payload)

    def build_signin_payload(self, email, password):
        return {
            "email": email,
            "password": password
        }

    def signin_request(self, payload):
        return self.client.post("/api/auth/token/login/", payload)
