import locale

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, \
    KeyboardButton

# отображение даты на русском языке
locale.setlocale(category=locale.LC_ALL, locale='ru_RU.UTF-8')


def create_main_menu_buttons() -> InlineKeyboardMarkup:
    """Создаёт кнопки главного меню."""
    btn_hours_news = InlineKeyboardButton(text='Получить новости за последний час', callback_data='HOURS NEWS')
    btn_days_news = InlineKeyboardButton(text='Получить новости за последние сутки', callback_data='DAYS NEWS')
    btn_add_source = InlineKeyboardButton(text='Добавить источник', callback_data=f'GET SOURCES')
    bth_help = InlineKeyboardButton(text='Помощь', callback_data=f'HELP')

    first_row = [btn_hours_news]
    second_row = [btn_days_news]
    third_row = [btn_add_source]
    fourth_row = [bth_help]
    rows = [first_row, second_row, third_row, fourth_row]

    return InlineKeyboardMarkup(inline_keyboard=rows)
