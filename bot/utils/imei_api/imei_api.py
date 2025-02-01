import requests
from config import config

class ImeiApi:
    def __init__(self, token: str):
        self.token: str = token
        self.HEADERS = {
            'Content-type': 'application/json',
        }

    def check(self, imei_number: str):
        data = {
            'token': self.token,
            'imei_number': imei_number,
        }
        res = requests.post(config.backend_url + "/app/check-imei", json=data, headers=self.HEADERS)
        return res.json()

