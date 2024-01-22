from aiogram import Router
from aiogram.filters import Command

from handlers.proponent.handler import proponent_handler

proponent_router = Router()
proponent_router.message.register(proponent_handler, Command('proponent'))
