from .imei_api import ImeiApi
from config import config


def check_imei(imei_number: str):
    imei_api = ImeiApi(token=config.backend_token.get_secret_value())
    return imei_api.check(imei_number)
