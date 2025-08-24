from aiogram import Router
from aiogram import F
from aiogram.types import Message
from keyboards import main_menu_kb,kbju_kb

message_router = Router(name="message_router")

@message_router.message(F.text=="Вес")
async def weight_handler(message: Message):
    await message.answer("Вес")

@message_router.message(F.text=="Вода")
async def water_handler(message: Message):
    await message.answer("Вода")

@message_router.message(F.text=="КБЖУ")
async def kbju_handler(message: Message):
    await message.answer("Выберите подраздел", reply_markup=kbju_kb())

@message_router.message(F.text=="Съеденное КБЖУ")
async def today_kbju_handler(message: Message):
    await message.answer("Съеденное КБЖУ", reply_markup=kbju_kb())

@message_router.message(F.text=="Добавить блюдо/продукт в КБЖУ")
async def add_today_kbju_handler(message: Message):
    await message.answer("Добавить блюдо/продукт в КБЖУ", reply_markup=kbju_kb())

@message_router.message(F.text=="Создать блюдо/продукт в список")
async def add_dishes_list_handler(message: Message):
    await message.answer("Создать блюдо/продукт в список", reply_markup=kbju_kb())

@message_router.message(F.text=="Назад")
async def return_main_menu_handler(message: Message):
    await message.answer("Главное меню", reply_markup=main_menu_kb())