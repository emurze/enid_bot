import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from dispatcher import get_dispatcher

lg = logging.getLogger(__name__)


async def main(dp: Dispatcher = get_dispatcher()) -> None:
    lg.info('BOT IS RUNNING')
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await asyncio.Task(dp.start_polling(bot))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
