from aiogram import Bot

from .bot_config import TOKEN

bot = Bot(token=TOKEN)

# Функция для отправки ссылки подтверждения
async def send_telegram_verification_link(chat_id, token):
    link = f"https://127.0.0.1:8000/api/verify-telegram/{token}/"
    text = f"Для подтверждения аккаунта перейдите по ссылке:\n{link}"
    await bot.send_message(chat_id, text)