import asyncio

from aiogram.types import Message

from handlers.hero import parser
from handlers.hero.constants import URL
from helpers.tasks import create_cpu_task
from helpers.web import make_text_from_url


async def hero_handler(message: Message) -> None:
    response = await make_text_from_url(URL)

    async with asyncio.TaskGroup() as tg:
        collected_signatures = tg.create_task(
            create_cpu_task(parser.parse_collected_signatures, response)
        )
        left_signatures = tg.create_task(
            create_cpu_task(parser.parse_left_signatures, response)
        )

    collected_votes = ''.join(collected_signatures.result())
    left_votes = ''.join(left_signatures.result())

    await message.answer(
        f"{collected_votes} votes collected\n"
        f"{left_votes} votes remain"
    )
