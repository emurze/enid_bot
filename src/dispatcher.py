from aiogram import Dispatcher

from handlers.start.router import base_router
from handlers.person.router import person_router
from handlers.proponent.router import proponent_router


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(base_router)
    dp.include_router(person_router)
    dp.include_router(proponent_router)
    return dp
