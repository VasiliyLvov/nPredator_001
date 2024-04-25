import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
@dp.message(Command(commands=['старт']))
async def start(message: types.Message):
    await message.answer(f'Привет, друг {message.from_user.full_name}!\n'
                         f'Примените команду /info для получения более подробной информации')

@dp.message(Command(commands=['stop']))
@dp.message(Command(commands=['стоп']))
async def start(message: types.Message):
    await message.answer(f'Пока, {message.from_user.full_name}!')

@dp.message(Command(commands=['info']))
@dp.message(Command(commands=['инфо']))
async def start(message: types.Message):
    await message.answer('Этот бот предназначен для экспериментов с различными нейросетями.\n'
                         'На данный момент бот ограничен в функционале.\n'
                         'Доступные команды:\n'
                         '/start /старт - приветственное сообщение\n'
                         '/stop /стоп - прощальное сообщение\n'
                         '/info /инфо - информация о боте\n'
                         '/user /пользователь - выводит информацию о пользователе')

@dp.message(Command(commands=['user']))
@dp.message(Command(commands=['пользователь']))
async def start(message: types.Message):
    await message.answer(f'Данные пользователя, {message.from_user}!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())