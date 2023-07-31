from typing import Callable

from aiogram.types import Message


def is_private_chat(func: Callable):
    async def wrapper(message: Message):
        if message.chat.type == 'private':
            await func(message)
    return wrapper
