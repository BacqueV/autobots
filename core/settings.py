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
    port: int
    database: str

    def get_dsn(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


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
            port=env.str("DB_PORT"),
            database=env.str("DB_NAME"),
        ),
    )


settings = get_settings(".env")
