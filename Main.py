import asyncio
from config import get_api_token
from aiogram import Bot, Dispatcher
from handlers import main_router

bot = Bot(get_api_token())
dp = Dispatcher()


async def main() -> None:
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
