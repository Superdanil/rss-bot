import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

import config

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.username}")


@dp.message(Command("help"))
async def start(message: types.Message):
    await message.answer(text=f"Just an echo bot")


@dp.message()
async def echo_message(message: types.Message):
    await message.bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second..."
    )
    await message.reply(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())