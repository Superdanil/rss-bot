from aiogram.fsm.state import StatesGroup, State


class AddSourceState(StatesGroup):
    """Машина состояний для добавления нового источника новостей."""
    ADD_SOURCE_START = State()
    ADD_SOURCE_DONE = State()
