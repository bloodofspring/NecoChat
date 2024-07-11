from modules.processes.BaseHandler import BaseHandler
from pyrogram import handlers, types

from modules.util import UserManager
from modules.filters import in_interactive_dict_filter
from modules.config import analyzer


class InteractiveProcess(BaseHandler):
    __name__ = "Интерактивный regexp"
    HANDLER = handlers.MessageHandler
    FILTER = in_interactive_dict_filter

    async def func(self, _, message: types.Message):
        text = message.text.split()
        first_word = text[0]
        anal_version = analyzer.parse(first_word)[0]

        text[0] = anal_version.inflect({"masc", "perf"})[0]  # + "(а)"
        text = ["{}"] + [text[0]] + ["{}"] + text[1:]

        result = " ".join(text).format(
            UserManager(message.from_user, message.chat).from_database.custom_name,
            UserManager(message.reply_to_message.from_user, message.chat).from_database.custom_name
        )

        await message.reply(result)