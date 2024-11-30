from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from core.utils.db_api import Database


router = Router()
db = Database()


@router.message(CommandStart())
async def start(message: Message):
    name = message.from_user.username

    user = await db.select_user(message.from_user.id)
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
        await message.answer(f"Здравствуй, {name}, приветствую еще раз!")
