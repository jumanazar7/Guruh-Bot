from loader import dp
from filters import IsGroup
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(IsGroup(), CommandHelp())
async def answer_group(message: types.Message):
    member = message.from_user.full_name
    await message.reply(f"{member} sizga qanday yordam kerak!")
