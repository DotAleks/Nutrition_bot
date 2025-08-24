from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from keyboards import main_menu_kb

command_router = Router(name="command_router")


@command_router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("/start", reply_markup=main_menu_kb())
