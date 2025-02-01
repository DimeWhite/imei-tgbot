import asyncio

from aiogram import Bot, Dispatcher
from config import config
from handlers import get_routers
from middlewares import L10nMiddleware, WhiteListMessageMiddleware
from fluent_loader import get_fluent_localization


async def main():
    locale = get_fluent_localization()

    dp = Dispatcher()
    dp.message.outer_middleware(L10nMiddleware(locale))
    dp.pre_checkout_query.outer_middleware(L10nMiddleware(locale))

    dp.message.outer_middleware(WhiteListMessageMiddleware(config.whitelist))
    dp.pre_checkout_query.outer_middleware(WhiteListMessageMiddleware(config.whitelist))

    dp.include_routers(*get_routers())

    bot = Bot(config.bot_token.get_secret_value())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
