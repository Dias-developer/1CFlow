# aiogram
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def inline_choose_file_type():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Excel', callback_data='excel')],
            [InlineKeyboardButton(text='PDF', callback_data='pdf')],
            [InlineKeyboardButton(text='Фото/Скрин', callback_data='ocr')],
        ]
    )
    return keyboard