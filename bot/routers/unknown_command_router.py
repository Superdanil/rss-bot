from aiogram import Router, types

router = Router()


@router.message()
async def unknown_command_message(message: types.Message):
    """Отвечает на сообщения пользователя, не попавшие ни в один обработчик."""
    await message.reply(text="Unknown command💭")
