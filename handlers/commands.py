# aiogram
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# from different py.files
from Project.keyboards.inline.choose_file_type import inline_choose_file_type

router = Router()

@router.message(Command('start'))
async def greeting(message: Message):
    await message.answer('Привет! Я бот для автоматизаций ручного ввода в 1C', reply_markup=inline_choose_file_type())
