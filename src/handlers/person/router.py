from aiogram import Router
from aiogram.filters import Command

from handlers.person.handler import person_handler

person_router = Router()
person_router.message.register(person_handler, Command('person'))
