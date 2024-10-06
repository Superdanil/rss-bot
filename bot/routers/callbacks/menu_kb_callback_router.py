from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from fsm import AddSourceState
from routers.commands.support_router import help_message
from services import news_service

router = Router()


@router.callback_query(F.data == 'HOURS NEWS')
async def handle_hours_news_btn(callback: CallbackQuery):
    """Отправляет новости за последний час."""
    msg = await news_service.get_news(data=callback, hours=1)
    await callback.message.answer(text=msg)


@router.callback_query(F.data == 'DAYS NEWS')
async def handle_days_news_btn(callback: CallbackQuery):
    """Отправляет новости за последние 24 часа."""
    msg = await news_service.get_news(data=callback, hours=24)
    await callback.message.answer(text=msg)


@router.callback_query(F.data == 'ADD SOURCE')
async def handle_add_source_btn(callback: CallbackQuery, state: FSMContext):
    await news_service.add_source_start(message=callback.message, state=state)


@router.message(AddSourceState.ADD_SOURCE_START)
async def add_source(message: Message, state: FSMContext):
    await news_service.add_source_done(message=message, state=state)


@router.callback_query(F.data == 'HELP')
async def handle_help_btn(callback: CallbackQuery) -> Message:
    """Вызывает команду /help."""
    return await help_message(callback.message)
