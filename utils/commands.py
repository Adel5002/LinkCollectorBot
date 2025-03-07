from aiogram.filters.command import Command, BotCommand

commands = [
    BotCommand(command='/commands', description='Доступные команды'),
    BotCommand(command='/link_collector', description='для сбора ссылок в csv файл'),
    BotCommand(command='/other_command', description='Другая команда...')
]