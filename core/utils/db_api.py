from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from core.settings import settings


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=settings.connection.user,
            password=settings.connection.password,
            host=settings.connection.host,
            database=settings.connection.database,
        )

    async def disconnect(self):
        if self.pool is not None:
            await self.pool.close()

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def list_users(self):
        sql = "SELECT * FROM users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = "SELECT * FROM users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def update_user_data(self, full_name, username, telegram_id):
        sql = "UPDATE users SET full_name=$1, username=$2 WHERE telegram_id=$3"
        return await self.execute(sql, full_name, username, telegram_id, execute=True)
