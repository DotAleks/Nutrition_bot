from aiogram import Router
from aiogram import F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import main_menu_kb, kbju_kb
from utils import is_valid_weight,is_valid_water,is_number

message_router = Router(name="message_router")

Calories = 2000
Proteins = 143
Fats = 52
Carbohydrates = 143

class WeightState(StatesGroup):
    weight = State()

class WaterState(StatesGroup):
    water = State()

class ProductState(StatesGroup):
    name = State()
    calories = State()
    proteins = State()
    fats = State()
    carbohydrates = State()
    unit = State()

class DishState(StatesGroup):
    Name = State()
    Products = State()
    Description = State()

@message_router.message(F.text == "Вес")
async def weight_handler(message: Message, state: FSMContext):
    await state.set_state(WeightState.weight)
    await message.answer("Введите вес", reply_markup=ReplyKeyboardRemove())

@message_router.message(WeightState.weight)
async def process_weight(message: Message, state: FSMContext):
    result, is_valid = is_valid_weight(message.text)# type: ignore
    
    if is_valid:
        await state.update_data(weight=result)
        
        data = await state.get_data()
        weight = data.get('weight')
        
        await message.answer(f"Вес {weight} кг сохранен!", reply_markup=main_menu_kb())
        await state.clear()
    else:
        await message.answer(result)

@message_router.message(F.text == "Вода")
async def water_handler(message: Message,state:FSMContext):
    await state.set_state(WaterState.water)
    await message.answer("Введите количество выпитой воды",reply_markup=ReplyKeyboardRemove())

@message_router.message(WaterState.water)
async def process_water(message: Message, state: FSMContext):
    result,is_valid = is_valid_water(message.text) #type: ignore

    if is_valid:
        await state.update_data(water=result)
        data = await state.get_data()
        water = data.get('water')
        await message.answer(f"Вода {water} мл сохранена!", reply_markup=main_menu_kb())
        await state.clear()
    else:
        await message.answer(result)# type: ignore

@message_router.message(F.text == "КБЖУ")
async def kbju_handler(message: Message):
    await message.answer("Выберите подраздел", reply_markup=kbju_kb())

temp1=100

@message_router.message(F.text == "Съеденное КБЖУ")
async def today_kbju_handler(message: Message):
    text = f"Калории: {temp1}/{Calories}\nБелки: {temp1}/{Proteins}\nЖиры: {temp1}/{Fats}\nУглеводы: {temp1}/{Carbohydrates}\n"
    await message.answer(text, reply_markup=kbju_kb())

@message_router.message(F.text == "Добавить блюдо/продукт в КБЖУ")
async def add_today_kbju_handler(message: Message,state:FSMContext):
    await state.set_state(ProductState.name)
    await message.answer("Введите название продукта", reply_markup=kbju_kb())

@message_router.message(ProductState.name)
async def process_name(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(ProductState.calories)
    await message.answer("Введите количество ккал на 100 грамм")

@message_router.message(ProductState.calories)
async def process_calories(message: Message, state:FSMContext):
    if is_number(message.text):
        await state.update_data(calories=message.text)
        await state.set_state(ProductState.proteins)
        await message.answer("Введите количество белка на 100 грамм")
    else:
        await message.answer("Введите число!")

@message_router.message(ProductState.proteins)
async def process_proteins(message: Message, state:FSMContext):
    if is_number(message.text):
        await state.update_data(proteins=message.text)
        await state.set_state(ProductState.fats)
        await message.answer("Введите количество жира на 100 грамм")
    else:
        await message.answer("Введите число!")

@message_router.message(ProductState.fats)
async def process_fats(message: Message, state:FSMContext):
    if is_number(message.text):
        await state.update_data(fats=message.text)
        await state.set_state(ProductState.carbohydrates)
        await message.answer("Введите количество углеводов на 100 грамм")
    else:
        await message.answer("Введите число!")

@message_router.message(ProductState.carbohydrates)
async def process_carbohydrates(message: Message, state:FSMContext):
    if is_number(message.text):
        await state.update_data(carbohydrates=message.text)
        await state.set_state(ProductState.unit)
        await message.answer("Введите единицу измерения")
    else:
        await message.answer("Введите число!")

@message_router.message(ProductState.unit)
async def process_unit(message: Message, state:FSMContext):
    await state.update_data(unit=message.text)
    data = await state.get_data()
    await message.answer(f"Добавлен продукт {data["name"]}\nКалории: {data["calories"]}\nБелки: {data["proteins"]}\n Жиры: {data["fats"]}\nУглеводы: {data["carbohydrates"]}\nЕдиница измерения: {data["unit"]}")

@message_router.message(F.text == "Создать блюдо/продукт в список")
async def add_dishes_list_handler(message: Message):
    await message.answer("Создать блюдо/продукт в список", reply_markup=kbju_kb())

@message_router.message(F.text == "Назад")
async def return_main_menu_handler(message: Message):
    await message.answer("Главное меню", reply_markup=main_menu_kb())