import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard_001, keyboard_empty
import subrcs

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
@dp.message(F.text.lower() == 'старт')
@dp.message(F.text.lower() == 'начать')
async def start(message: types.Message):
    await message.answer(f'Привет, друг {message.from_user.full_name}!\n'
                         f'Примени команду /info для получения более подробной информации', reply_markup=keyboard_001)

@dp.message(Command(commands=['stop']))
@dp.message(F.text.lower() == 'стоп')
@dp.message(F.text.lower() == 'закончить')
async def start(message: types.Message):
    await message.answer(f'Пока, {message.from_user.full_name}!', reply_markup=keyboard_empty)

@dp.message(Command(commands=['info']))
@dp.message(F.text.lower() == 'инфо')
async def start(message: types.Message):
    await message.answer(subrcs.get_info_message())

@dp.message(Command(commands=['user']))
@dp.message(F.text.lower() == 'пользователь')
async def start(message: types.Message):
    await message.answer(f'Данные пользователя, {message.from_user}!')

@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'что ты умеешь' in message.text.lower() or 'что умеешь' in message.text.lower():
        await message.reply(subrcs.get_info_message(), reply_markup=keyboard_001)
    elif 'хорошо' in message.text.lower() or 'нормально' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    else:
        await message.reply('Не понимаю тебя...')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())