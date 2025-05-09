import asyncio
import logging
from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher
from ...bot_config import TOKEN
from ...handlers.commands import router


class Command(BaseCommand):
    help = 'Runs the Telegram bot.'

    def handle(self, *args, **kwargs):
        asyncio.run(self.run_bot())

    async def run_bot(self):
        logging.basicConfig(level=logging.INFO)
        bot = Bot(token=TOKEN)
        dp = Dispatcher()
        dp.include_router(router)

        await dp.start_polling(bot)
