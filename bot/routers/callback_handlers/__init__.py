from aiogram import Router

from .menu_kb_callback_handlers import router as menu_kb_callback_router

router = Router(name=__name__)

router.include_routers(menu_kb_callback_router)
