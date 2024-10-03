from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data)
async def handle_main_menu(callback_query: CallbackQuery):
    await callback_query.answer("hkbgfhbgfhj")