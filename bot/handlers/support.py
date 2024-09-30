from aiogram import Router, types
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.first_name}")


@router.message(Command("help"))
async def help_message(message: types.Message):
    await message.answer(text=f"Just an echo bot")


@router.message()
async def echo_message(message: types.Message):
    await message.reply(text="Unknown command💭")
