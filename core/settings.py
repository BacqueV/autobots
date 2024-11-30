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
            user=env.str("USER"),
            password=env.str("PASSWORD"),
            host=env.str("HOST"),
            database=env.str("DATABASE"),
        ),
    )


settings = get_settings(".env")
