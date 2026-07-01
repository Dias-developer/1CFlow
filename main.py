# aiogram
from aiogram import Dispatcher, Bot

# python
import logging
from os import getenv
from dotenv import load_dotenv
from asyncio import run

# from different py.files
from handlers import commands
from handlers.callbacks import choose_file_type
from handlers import getting_files

load_dotenv()
token = getenv('TOKEN')
dp = Dispatcher()


async def main():

    dp.include_router(commands.router)
    dp.include_router(choose_file_type.router)
    dp.include_router(getting_files.router)

    bot = Bot(token=getenv('TOKEN'))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print('Start...')
    try:
        run(main())
    except KeyboardInterrupt:
        print('Stop...')