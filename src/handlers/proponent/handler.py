import logging

from aiogram.types import Message

from handlers.proponent.scraper import scrap_top_videos
from helpers.driver import DriverSession
from helpers.tasks import sync_to_async

lg = logging.getLogger(__name__)


async def proponent_handler(message: Message) -> None:
    lg.info('PROPONENT HANDLER')
    await message.answer('Please, wait several seconds...')

    async with DriverSession() as driver:
        data = await sync_to_async(scrap_top_videos, driver)

    lg.info(str(data))

    for title, link in data:
        await message.answer(title)
        await message.answer(link)
