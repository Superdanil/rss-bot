from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("add"))
async def add_origin(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.username}")


@router.message(Command("hour"))
async def get_news_for_the_last_hour(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.username}")


@router.message(Command("day"))
async def get_news_for_the_last_day(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.username}")


@router.message(Command("del"))
async def delete_origin(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.username}")
