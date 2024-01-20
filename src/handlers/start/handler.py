from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


async def start_handler(message: Message) -> None:
    button_hero = KeyboardButton(text='/hero')
    button_katz = KeyboardButton(text='/katz')

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button_hero, button_katz]],
        resize_keyboard=True
    )

    await message.answer("Hello bro", reply_markup=keyboard)
