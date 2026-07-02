from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Project.states.state1 import GetFiles
from Project.services.parser_excel import parse_excel

router = Router()
@router.message(F.document)
async def get_excel(message: Message, state: FSMContext):

    filename = message.document.file_name

    if filename.endswith(('.xlsx', '.xls')):
        await message.answer(f'Получен файл: {filename}')

        await state.update_data(filename=filename)

        await parse_excel(message)

    else:
        await message.answer('Отправьте Excel файл!')