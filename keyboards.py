from aiogram import types

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

keyboard_001 = [
[button_001, button_002, button_003],
[button_004, button_005, button_006],
[button_007, button_008],
[button_009, button_010]
]

keyboard_001 = types.ReplyKeyboardMarkup(keyboard=keyboard_001, resize_keyboard=True)
keyboard_empty = types.ReplyKeyboardRemove()