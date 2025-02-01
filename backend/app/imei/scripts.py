import requests
from pydantic import Json

from config import config


def imeaCheckAPI(imea_number: str) -> Json:
    URL = "https://api.imeicheck.net/v1/checks"
    TOKEN = config.imeicheck_token.get_secret_value()
    headers = {
        "Authorization": "Bearer " + TOKEN,
        "Accept-Language": "en",
        "Content-Type": "application/json",
    }
    data = {
        "deviceId": imea_number,
        "serviceId": 12
    }
    res = requests.post(url=URL, headers=headers, json=data)
    if res.status_code == 422:
        return {'type': 'valid error'}
    elif res.status_code != 201:
        return {'type': 'system error'}
    return res.json()
