import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Логирование в консоль
        logging.FileHandler("bot.log", mode="a"),  # Логирование в файл
    ],
)

logger = logging.getLogger(__name__)
