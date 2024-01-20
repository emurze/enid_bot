from aiogram import Router
from aiogram.filters import Command

from handlers.hero.handler import hero_handler

hero_router = Router()
hero_router.message.register(hero_handler, Command('hero'))
