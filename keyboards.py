from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_001 = types.KeyboardButton(text='/start')
button_002 = types.KeyboardButton(text='Старт')
button_003 = types.KeyboardButton(text='Начать')
button_004 = types.KeyboardButton(text='/stop')
button_005 = types.KeyboardButton(text='Стоп')
button_006 = types.KeyboardButton(text='Закончить')
button_007 = types.KeyboardButton(text='/info')
button_008 = types.KeyboardButton(text='Инфо')
button_009 = types.KeyboardButton(text='/user')
button_010 = types.KeyboardButton(text='Пользователь')
button_011 = types.KeyboardButton(text='/career')
button_012 = types.KeyboardButton(text='Карьера')

keyboard_001 = [
[button_001, button_002, button_003],
[button_004, button_005, button_006],
[button_007, button_008],
[button_009, button_010],
[button_011, button_012]
]

keyboard_001 = types.ReplyKeyboardMarkup(keyboard=keyboard_001, resize_keyboard=True)

def make_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    keyboard = ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    return keyboard