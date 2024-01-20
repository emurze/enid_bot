import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from dispatcher import get_dispatcher


async def main(dp: Dispatcher = get_dispatcher()) -> None:
    print('BOT IS RUNNING')
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await asyncio.Task(dp.start_polling(bot))


if __name__ == '__main__':
    asyncio.run(main())
