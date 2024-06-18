import asyncio
from create_bot import bot, dp, admins
from db_handler.db_funk import get_all_users
from handlers.admin_panel import admin_router
from handlers.user_router import user_router
from aiogram.types import BotCommand, BotCommandScopeDefault


# Функция, которая настроит командное меню (дефолтное для всех пользователей)
async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='profile', description='Мой профиль')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# Функция, которая выполнится когда бот запустится
async def start_bot():
    await set_commands()
    count_users = await get_all_users(count=True)
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, f'Я запущен🥳. Сейчас в базе данных <b>{count_users}</b> пользователей.')
    except:
        pass


# Функция, которая выполнится когда бот завершит свою работу
async def stop_bot():
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, 'Бот остановлен. За что?😔')
    except:
        pass


async def main():
    # регистрация роутеров
    dp.include_router(user_router)
    dp.include_router(admin_router)

    # регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
