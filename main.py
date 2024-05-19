import asyncio
import config
from aiogram import Bot, Dispatcher
import logging
import subrcs, career

async def main():

    #Логирование
    logging.basicConfig(level=logging.INFO)

    # Объект бота и диспетчера
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_router(career.router)
    dp.include_router(subrcs.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())