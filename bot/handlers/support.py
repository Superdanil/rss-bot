import httpx
from aiogram import Router, types
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer(text=f"Доброго времени суток, {message.from_user.first_name}")
    with httpx.Client() as client:
        client.post(
            url="http://127.0.0.1:8000/users",
            headers={"Content-Type": "application/json"},
            json={"telegram_id": message.from_user.id},
        )


@router.message(Command("help"))
async def help_message(message: types.Message):
    await message.answer(text=f"Just an echo bot")


@router.message()
async def echo_message(message: types.Message):
    await message.reply(text="Unknown command💭")
