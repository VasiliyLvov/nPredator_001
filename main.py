import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters.command import Command
import logging
# import random
# from keyboards import keyboard_001, keyboard_empty
import subrcs

async def main():

    #Логирование
    logging.basicConfig(level=logging.INFO)

    # Объект бота и диспетчера
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_router(subrcs.router)
#    dp.include_router(msgs.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())