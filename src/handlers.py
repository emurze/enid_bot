import logging

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

lg = logging.getLogger(__name__)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()

    for index in range(1, 11):
        builder.button(text=f"Set {index}", callback_data=f"set:{index}")

    await message.answer("Hello", reply_markup=builder.as_markup())


@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer('HELP')
