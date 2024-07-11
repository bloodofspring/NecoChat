from . import BaseHandler as B
from pyrogram import handlers, filters, types


class StartProcess(B.BaseHandler):
    __name__ = "Обработчик команды /start"
    HANDLER = handlers.MessageHandler
    FILTER = filters.command("start")

    async def func(self, _, message: types.Message):
        await message.reply(f"Привет, <b>{message.from_user.first_name.title()}</b>!")