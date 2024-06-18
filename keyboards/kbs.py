from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import admins


def main_kb(user_telegram_id: int):
    kb_list = [[KeyboardButton(text="👤 Мой профиль")]]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )


def home_page_kb(user_telegram_id: int):
    kb_list = [[KeyboardButton(text="🔙 Назад")]]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
