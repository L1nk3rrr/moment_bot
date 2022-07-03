from aiogram.dispatcher.filters import BoundFilter

from tg_bot.services import sqlite_db


class Register(BoundFilter):
    key = "not_exist"

    def __init__(self, not_exist=None):
        self.not_exist = not_exist

    async def check(self, obj):
        if await sqlite_db.get_user_name(obj.from_user.id):
            return False
        else:
            return True

