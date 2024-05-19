from aiogram import Router, types, F
from aiogram.filters.command import Command
import msgs
import keyboards
from utils.apis import fox

router = Router()

@router.message(Command(commands=['start']))
@router.message(F.text.lower() == 'старт')
@router.message(F.text.lower() == 'начать')
async def start(message: types.Message):
    await message.answer(f'Привет, друг {message.from_user.full_name}!\n'
                         f'Примени команду /info для получения более подробной информации',
                         reply_markup=keyboards.make_main_kb())

@router.message(Command(commands=['stop']))
@router.message(F.text.lower() == 'стоп')
@router.message(F.text.lower() == 'закончить')
async def stop(message: types.Message):
    await message.answer(f'Пока, {message.from_user.full_name}!\n'
                         'Чтобы начать заново используй /start',
                         reply_markup=types.ReplyKeyboardRemove())

@router.message(Command(commands=['info']))
@router.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    await message.answer(msgs.get_info_message())

@router.message(Command(commands=['user']))
@router.message(F.text.lower() == 'пользователь')
async def user(message: types.Message):
    await message.answer(f'Данные пользователя, {message.from_user}!')

@router.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'что ты умеешь' in message.text.lower() or 'что умеешь' in message.text.lower():
        await message.reply(msgs.get_info_message(), reply_markup=keyboards.make_main_kb())
    elif 'хорошо' in message.text.lower() or 'нормально' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    elif 'лиса' in message.text.lower() or 'покажи лису' in message.text.lower():
        img_fox = fox()
        await message.answer('Лови лису')
        await message.answer_photo(img_fox)
    else:
        await message.reply('Не понимаю тебя...')