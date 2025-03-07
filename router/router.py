from aiogram import Router
from modules import start, get_links

def register_routers() -> Router:
    router = Router()

    router.include_router(start.router)
    router.include_router(get_links.router)
    return router