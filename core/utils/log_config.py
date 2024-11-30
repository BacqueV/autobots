import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    filename="bot.log",  # Имя файла для логов
    filemode="a",  # Режим записи: "a" - добавление, "w" - перезапись
)

logger = logging.getLogger(__name__)
