# aiogram
from aiogram import Router, F
from aiogram.types import Message

# .py files from different files
from Project.services.parser_excel import parse_excel

router = Router()


@router.message(F.document)
async def get_excel(message: Message):

    filename = message.document.file_name

    if filename.endswith(('.xlsx', '.xls')):
        await message.answer(
            f"Получил файл: {filename}"
        )

        await parse_excel(message)

    elif filename.endswith('.pdf'):
        await message.answer(
            f"Получил файл:: {filename}"
        )

    else:
        await message.answer(
            "Пожалуйста, отправьте Excel или PDF файл"
        )