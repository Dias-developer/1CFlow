# aiogram
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
# from different py.files
from Project.keyboards.inline.choose_file_type import inline_choose_file_type
from Project.states.state1 import GetFiles
router = Router()

@router.message(Command('start'))
async def greeting(message: Message, state: FSMContext):
    await message.answer('Привет! Я бот для автоматизаций ручного ввода в 1C', reply_markup=inline_choose_file_type())

    await state.set_state(GetFiles.choosing_type)