from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio

from core.settings import settings
from core.handlers import get_routers
from core.utils.set_bot_commands import set_bot_commands
from core.utils.log_config import logger
from container import DBContainer

bot = Bot(token=settings.bot.token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
container = DBContainer()


@dp.startup.register
async def on_startup():
    # initializing connection pool
    await container.db_pool()

    db = container.db()
    await db.create_table_users()
    await set_bot_commands(bot)
    logger.info("Бот успешно запущен!")


@dp.shutdown.register
async def on_shutdown():
    db = container.get("db")
    await db.disconnect()
    await bot.session.close()
    logger.info("Бот успешно завершил работу.")


async def start():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        dp.include_routers(*get_routers())
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
