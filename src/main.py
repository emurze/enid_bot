import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from handlers import dp


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await asyncio.Task(dp.start_polling(bot))


if __name__ == '__main__':
    asyncio.run(main())
