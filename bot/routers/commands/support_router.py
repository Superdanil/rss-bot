from aiogram import Router, types
from aiogram.filters import CommandStart, Command

import keyboards as kb
from services import database_service
from exceptions import DatabaseError

router = Router()


@router.message(CommandStart())
async def start_message(message: types.Message):
    """Обрабатывает команду /start."""
    try:
        await database_service.register_user(telegram_id=message.from_user.id)
        await message.answer(text=f"Доброго времени суток, {message.from_user.first_name}")
        buttons = kb.create_menu_buttons()
        await message.answer("Прочитать новостную ленту:", reply_markup=buttons)
    except DatabaseError:
        await message.answer("Простите, сервис временно недоступен.")


@router.message(Command("help"))
async def help_message(message: types.Message):
    """Обрабатывает команду /help."""
    await message.answer(
        text="/hour - новостная лента за последний час\n"
        "/day - новостная лента за последние 24 часа\n"
        "/add - добавить ссылку на новостной источник\n",
    )
