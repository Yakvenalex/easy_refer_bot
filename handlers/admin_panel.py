from aiogram import F, Router
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from create_bot import admins, bot
from db_handler.db_funk import get_all_users
from keyboards.kbs import home_page_kb

admin_router = Router()


@admin_router.message((F.text.endswith('Админ панель')) & (F.from_user.id.in_(admins)))
async def get_profile(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        all_users_data = await get_all_users()

        admin_text = (
            f'👥 В базе данных <b>{len(all_users_data)}</b> человек. Вот короткая информация по каждому:\n\n'
        )

        for user in all_users_data:
            admin_text += (
                f'👤 Телеграм ID: {user.get("user_id")}\n'
                f'📝 Полное имя: {user.get("full_name")}\n'
            )

            if user.get("user_login") is not None:
                admin_text += f'🔑 Логин: {user.get("user_login")}\n'

            if user.get("refer_id") is not None:
                admin_text += f'👨‍💼 Его пригласил: {user.get("refer_id")}\n'

            admin_text += (
                f'👥 Он пригласил: {user.get("count_refer")} человек\n'
                f'📅 Зарегистрирован: {user.get("date_reg")}\n'
                f'\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n'
            )

    await message.answer(admin_text, reply_markup=home_page_kb(message.from_user.id))
