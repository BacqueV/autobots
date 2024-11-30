from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio

from aiogram.types import users_shared
from core.settings import settings
from core.handlers import get_routers
from core.utils.db_api import Database
from core import handlers


async def start():
    bot = Bot(token=settings.bot.token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    dp.include_routers(*get_routers())
    db = Database()

    try:
        await db.connect()
        await db.create_table_users()
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
