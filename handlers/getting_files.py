from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.document)
async def get_excel(message: Message):

    file_name = message.document.file_name

    await message.answer(
        f"Получил файл: {file_name}"
    )