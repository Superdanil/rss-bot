from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from fsm import AddSourceState
from services import database_service
from settings import settings


async def add_source_start(message: Message, state: FSMContext):
    """Принимает ссылку на RSS-источник."""
    await state.set_state(AddSourceState.ADD_SOURCE_START)
    await message.answer(text="Отправьте ссылку на rss-источник.")


async def add_source_done(message: Message, state: FSMContext):
    """Добавляет ссылку на RSS-источник в БД."""
    result = await database_service.add_source(telegram_id=message.from_user.id, message=message.text)

    if result:
        await message.answer(text=f"Подписка на {message.text} успешно добавлена")
    else:
        await message.answer(text="Неверные входные данные")

    await state.set_state(AddSourceState.ADD_SOURCE_DONE)


async def get_news(data: Message | CallbackQuery, hours: int) -> str:
    """Возвращает отформатированную строку со списком новостей."""
    newsfeed = await database_service.get_news(telegram_id=data.from_user.id, hours=hours)

    if newsfeed is None:
        return "Ошибка приложения"
    if len(newsfeed) == 0:
        return f"За последние {hours} час(а) ничего не произошло"
    return serialize_newsfeed(newsfeed)


def serialize_newsfeed(newsfeed: list[dict]) -> str:
    """Форматирует список новостей."""
    return "\n\n".join(f"{news['title']}\n{news['link']}" for news in newsfeed[: settings.NEWSFEED_LIMIT])
