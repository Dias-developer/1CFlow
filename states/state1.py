from aiogram.fsm.state import State, StatesGroup


class GetFiles(StatesGroup):
    choosing_type = State()

    waiting_excel = State()

    show_result = State()