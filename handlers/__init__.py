from aiogram import Router
from .commands import command_router
from .messages import message_router

main_router = Router(name="main_router")

main_router.include_router(command_router)
main_router.include_router(message_router)
__all__ = ["main_router"]
