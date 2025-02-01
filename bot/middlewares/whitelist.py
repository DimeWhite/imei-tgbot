from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class WhiteListMessageMiddleware(BaseMiddleware):
    def __init__(
        self,
        whitelist: Dict
    ):
        self.whitelist = whitelist

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.from_user.username not in self.whitelist:
            await event.reply("У вас нет доступа к этому боту.")
            return
        return await handler(event, data)