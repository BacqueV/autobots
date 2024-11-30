from environs import Env
from dataclasses import dataclass


@dataclass
class Bot:
    token: str


@dataclass
class Connection:
    user: str
    password: str
    host: str
    database: str


@dataclass
class Settings:
    bot: Bot
    connection: Connection


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bot=Bot(token=env.str("TOKEN")),
        connection=Connection(
            user=env.str("DB_USER"),
            password=env.str("DB_PASSWORD"),
            host=env.str("DB_HOST"),
            database=env.str("DB_NAME"),
        ),
    )


settings = get_settings(".env")
