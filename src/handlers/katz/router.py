from aiogram import Router
from aiogram.filters import Command

from handlers.katz.handler import katz_handler

katz_router = Router()
katz_router.message.register(katz_handler, Command('katz'))
