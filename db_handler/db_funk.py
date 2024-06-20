from sqlalchemy import Integer, String, BigInteger, TIMESTAMP
from create_bot import db_manager
import asyncio


# функция, которая создаст таблицу с пользователями
async def create_table_users(table_name='users_reg'):
    async with db_manager as client:
        columns = [
            {"name": "user_id", "type": BigInteger, "options": {"primary_key": True, "autoincrement": False}},
            {"name": "full_name", "type": String},
            {"name": "user_login", "type": String},
            {"name": "refer_id", "type": BigInteger},
            {"name": "count_refer", "type": Integer, "options": {"default": 0, "server_default": '0'}},
            {"name": "date_reg", "type": TIMESTAMP},
        ]
        await client.create_table(table_name=table_name, columns=columns)


# функция, для получения информации по конкретному пользователю
async def get_user_data(user_id: int, table_name='users_reg'):
    async with db_manager as client:
        user_data = await client.select_data(table_name=table_name, where_dict={'user_id': user_id}, one_dict=True)
    return user_data


# функция, для получения всех пользователей (для админки)
async def get_all_users(table_name='users_reg', count=False):
    async with db_manager as client:
        all_users = await client.select_data(table_name=table_name)
    if count:
        return len(all_users)
    else:
        return all_users


# функция, для добавления пользователя в базу данных
async def insert_user(user_data: dict, table_name='users_reg'):
    async with db_manager as client:
        await client.insert_data_with_update(table_name=table_name, records_data=user_data, conflict_column='user_id')
        if user_data.get('refer_id'):
            refer_info = await client.select_data(table_name=table_name,
                                                  where_dict={'user_id': user_data.get('refer_id')},
                                                  one_dict=True, columns=['user_id', 'count_refer'])
            await client.update_data(table_name=table_name,
                                     where_dict={'user_id': refer_info.get('user_id')},
                                     update_dict={'count_refer': refer_info.get('count_refer') + 1})

# asyncio.run(create_table_users())
