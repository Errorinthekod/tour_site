import asyncio
import sys, logging
from aiogram import Bot, Dispatcher
from megastart_tour_project.apps.telegram_bot.bot_config import TOKEN
from megastart_tour_project.apps.telegram_bot.handlers.commands import router
# from handlers.admin import admin_router




async def main():
    # await create_tables()
    # await add_category()
    bot = Bot(token = TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    # dp.include_router(admin_router)
    await dp.start_polling(bot) #start_polling - псотоянное ожидание запроса от пользователя


if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    asyncio.run(main())



