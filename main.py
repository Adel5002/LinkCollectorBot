import asyncio
import logging
import sys

from aiogram import Dispatcher

from utils.commands import commands
from router.router import register_routers
from bot import bot


async def main() -> None:
    dp = Dispatcher()
    await bot.set_my_commands(commands=commands)
    dp.include_router(register_routers())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())