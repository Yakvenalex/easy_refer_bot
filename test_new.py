from asyncpg_lite import DatabaseManager
import asyncio
from decouple import config

root_pass = config('ROOT_PASS')
autch_param = {'user': 'admin',
               'password': '15ox58cS',
               'host': '193.3.168.217',
               'port': 5432,
               'database': 'nadyaday_bot'}


async def main():
    db_manager = DatabaseManager(auth_params=autch_param, deletion_password=root_pass)
    async with db_manager:
        await db_manager.drop_table('new_users', password=root_pass)


asyncio.run(main())
