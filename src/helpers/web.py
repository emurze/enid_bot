import logging

from aiogram.client.session import aiohttp

from helpers.colors import c

lg = logging.getLogger(__name__)


async def make_request(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if str(response.status)[0] in ['4', '5']:
                lg.warning(f"{c.red}REQUEST PROBLEM{c.norm}")
            return await response.text()
