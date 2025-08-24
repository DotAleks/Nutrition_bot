from aiogram import Router
from .commands import router

main_router = Router(name="main_router")

main_router.include_router(router)
__all__ = ["main_router"]
