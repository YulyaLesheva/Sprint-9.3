import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=data, headers=headers)

    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=headers)
