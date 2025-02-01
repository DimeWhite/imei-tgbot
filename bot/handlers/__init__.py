from aiogram import Router

from . import imei


def get_routers() -> list[Router]:
    return [
        imei.router
    ]
