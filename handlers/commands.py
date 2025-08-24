from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from keyboards import main_menu_kb

router = Router(name="command_router")


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Text", reply_markup=main_menu_kb())
