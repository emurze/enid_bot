from aiogram import Dispatcher

from handlers.katz.router import katz_router
from handlers.start.router import base_router
from handlers.hero.router import hero_router


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(base_router)
    dp.include_router(hero_router)
    dp.include_router(katz_router)
    return dp
