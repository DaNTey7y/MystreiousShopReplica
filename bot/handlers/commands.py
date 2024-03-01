from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router()
router.message.filter(F.chat.type == "private")


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Привет, введи /help")


@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("🧬 Mysterious Shop 🧬\n\nКоманды:\n"
                         "/start - Старт\n/shop - Магазин\n/help - О боте\n\n"
                         "Разработчик:\n@xvhuqdph")


@router.message(Command("shop"))
async def shop_cmd(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="🧬 Mysterious Shop 🧬", switch_inline_query_current_chat=""))
    await message.answer("Нажми кнопку", reply_markup=builder.as_markup())
