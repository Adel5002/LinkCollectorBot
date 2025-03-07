from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router

from utils.commands import commands

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user.username == 'amka_developer':
        await message.reply('Hello my little gay boy')
    else:
        print(message.from_user.username)
        print(message.chat.id)
        print(message.message_thread_id)
        await message.answer(f'Greetings for you my honorable lord'
                             f' {message.from_user.full_name} 🙇‍♂️ \nНапиши /commands чтобы увидеть список команд')

@router.message(Command('commands', prefix="/", ignore_case=True))
async def list_of_commands(message: Message) -> None:
    await message.reply('\n'.join(f'{i.command} - {i.description}' for i in commands))