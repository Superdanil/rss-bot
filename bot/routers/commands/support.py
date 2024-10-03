import aiohttp
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
import bot.keyboards as kb
from bot.core.settings import settings

router = Router()


@router.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.first_name}")
    # async with aiohttp.ClientSession() as session:
    #     await session.post(
    #         url=f"{settings.database_url}/users",
    #         headers={"Content-Type": "application/json"},
    #         json={"telegram_id": message.from_user.id},
    #     )
    buttons = kb.create_main_menu_buttons()
    await message.answer("Прочитать новостную ленту:", reply_markup=buttons)


@router.message(Command("help"))
async def help_message(message: types.Message):
    await message.answer(text=f"/origins - список подключенных новостных источников"
                              f"/hour - новостная лента за последний час"
                              f"/day - новостная лента за последние 24 часа"
                              f"/add - добавить ссылку на новостной источник"
                              f"/del - отписаться от источника")


@router.message()
async def echo_message(message: types.Message):
    await message.reply(text="Unknown command💭")
