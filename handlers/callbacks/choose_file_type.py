from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == 'excel')
async def excel_choose_file_type(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Отправьте Excel файл!')


@router.callback_query(F.data == 'pdf')
async def pdf_file_type(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Отправьте PDF файл!')

@router.callback_query(F.data == 'ocr')
async def ocr_file_type(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Отправьте фото накладной!')

