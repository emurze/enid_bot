from aiogram.types import Message

from handlers.katz.constants import URL
from handlers.katz.parser import parse_top_videos
from helpers.web import make_text_from_url


async def katz_handler(message: Message) -> None:
    response = await make_text_from_url(URL)
    parse_top_videos(response)
