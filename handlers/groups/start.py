from loader import dp
from filters import IsGroup
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(IsGroup(), CommandStart())
async def answer_group(message: types.Message):
    member = message.from_user.full_name
    await message.reply(f"Assalomu aleykum, {member}. Tanishganimdan xursandman!")
