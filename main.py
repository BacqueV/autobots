from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio

from core.settings import settings
from core.handlers import get_routers
from core.utils.db_api import Database
from core.utils.set_bot_commands import set_bot_commands
from core.utils.log_config import logger


bot = Bot(token=settings.bot.token, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
db = Database()


# on_startup
@dp.startup.register
async def on_startup():
    print("hey")
    logger.warning("Инициализация бота...")
    logger.warning("Бот запускается...")
    await set_bot_commands(bot)
    logger.warning("Команды бота установлены.")
    logger.warning("Бот успешно запущен!")


# on_shutdown
@dp.shutdown.register
async def on_shutdown():
    logger.warning("Бот завершает работу...")
    await bot.session.close()
    logger.warning("Сессия HTTP клиента закрыта.")
    logger.warning("Бот успешно завершил работу.")


async def start():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        dp.include_routers(*get_routers())
        await db.connect()

        await db.create_table_users()

        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
