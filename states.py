from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    Region = State()
    Face = State()
    Support = State()



