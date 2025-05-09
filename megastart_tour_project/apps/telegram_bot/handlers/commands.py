from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Привет {message.from_user.full_name},   
     \n Я бот помощник. Я помогу Вам правильно зарегистрироваться.""")


@router.message(F.text == "/getid")
async def get_chat_id(message: Message):
    await message.answer(f"Ваш ID: {message.chat.id}")


