from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio
from core.settings import settings
from core import handlers


async def start():
    bot = Bot(token=settings.bot.token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
