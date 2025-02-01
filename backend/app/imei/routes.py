import json

from flask import Blueprint, jsonify
from flask_pydantic import validate
from pydantic import Json
from .models import IMEICheckModel
from config import config
from .scripts import imeaCheckAPI

main = Blueprint('main', __name__)
'''
Я бы сделал ручку. GET /app/check-imei/<imei_number>
Вместо того, чтоб отправлять токен в body. Я бы сделал это через header Authorization.
Токен бы получил сформировав его по логину и паролю присвоеному для конкретного бота
(Позволяет в будущем использовть API пользователям).
'''


@main.route('/app/check-imei', methods=["POST"])
@validate()
def imeiCheck(body: IMEICheckModel) -> Json:
    token = body.token
    imei_number = body.imei_number
    if token != config.bot_token_request.get_secret_value():
        return jsonify({"error": "401 Unauthorized"}), 401

    res = imeaCheckAPI(imei_number)
    if res["type"] == 'valid error':
        return jsonify({"error": "422 Validation Error"}), 422
    if res["type"] == 'system error':
        return jsonify({"error": "405 Server Error"}), 405
    return jsonify(res), 201
