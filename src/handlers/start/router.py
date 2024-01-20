from aiogram import Router
from aiogram.filters import Command

from handlers.start.handler import start_handler

base_router = Router()
base_router.message.register(start_handler, Command("start"))
