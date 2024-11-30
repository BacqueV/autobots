from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from core.utils.db_api import Database as db


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    name = message.from_user.username

    user = await db.select_user(telegram_id=message.from_user.id)
    if user is None:
        await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id,
        )
        await message.answer(f"Привет, {name}, рад познакомиться!")
    else:
        await db.update_user_data(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id,
        )
        await message.answer(f"здравствуй, {name}, приветствую еще раз!")
