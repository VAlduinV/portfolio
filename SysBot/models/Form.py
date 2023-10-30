from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    department = State()
    pc_number = State()
    problem_category = State()
    description = State()
    confirm = State()  # новое состояние
