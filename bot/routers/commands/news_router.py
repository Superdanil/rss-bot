from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services import news_service

router = Router()


@router.message(Command("add"))
async def add_origin(message: types.Message, state: FSMContext):
    await news_service.add_source_start(message=message, state=state)


@router.message(Command("hour"))
async def get_news_for_the_last_hour(message: types.Message):
    msg = await news_service.get_news(data=message, hours=1)
    await message.answer(text=msg)


@router.message(Command("day"))
async def get_news_for_the_last_day(message: types.Message):
    msg = await news_service.get_news(data=message, hours=24)
    await message.answer(text=msg)
