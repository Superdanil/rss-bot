import aiohttp
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

from bot.core.settings import settings

router = Router()


class AddSourceState(StatesGroup):
    ADD_SOURCE_START: State = State()
    ADD_SOURCE_DONE: State = State()


@router.callback_query(F.data == 'HOURS NEWS')
async def handle_hours_news_btn(callback: CallbackQuery) -> Message:
    async with aiohttp.ClientSession() as session:
        await session.post(
            url=f"{settings.database_url}/news",
            headers={"Content-Type": "application/json"},
            json={"telegram_id": callback.from_user.id, "timedelta": 1},
        )
    return await callback.message.answer(text="1")


@router.callback_query(F.data == 'DAYS NEWS')
async def handle_days_news_btn(callback: CallbackQuery) -> Message:
    return await callback.message.answer(text="2")


@router.callback_query(F.data == 'ADD SOURCE')
async def handle_add_source_btn(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddSourceState.ADD_SOURCE_START)
    return await callback.message.answer(text="Отправьте ссылку на rss-источник.")


@router.message(AddSourceState.ADD_SOURCE_START)
async def add_source(message: Message, state: FSMContext):
    async with aiohttp.ClientSession() as session:
        source = await session.post(
            url=f"{settings.database_url}/sources",
            headers={"Content-Type": "application/json"},
            json={"source": message.text, "telegram_id": message.from_user.id},
        )
        if source.status in (200, 201):
            await message.answer(text=f"Подписка на {message.text} успешно добавлена")
        else:
            await message.answer(text=f"Неверные входные данные")
    return await state.set_state(AddSourceState.ADD_SOURCE_DONE)


@router.callback_query(F.data == 'HELP')
async def handle_help_btn(callback: CallbackQuery) -> Message:
    msg = "ПАМАГИТИ"
    return await callback.message.answer(text=msg)
