from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


async def start_handler(message: Message) -> None:
    button_person = KeyboardButton(text='/person')
    button_proponent = KeyboardButton(text='/proponent')

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_person, button_proponent]],
        resize_keyboard=True
    )

    await message.answer("Dashboard", reply_markup=keyboard)
