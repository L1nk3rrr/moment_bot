from aiogram.dispatcher.filters import BoundFilter

import json, string

bad_words = {"сука", "блядь", "вбити", "згвалтувати", "тварь" ,"сука", "блять", "скривдити", "образити"}


class AdminFilter(BoundFilter):
    key = "is_bad"

    def __init__(self, is_bad=None):
        self.is_bad = is_bad

    async def check(self, obj):
        if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in obj.text.split(" ")} \
                .intersection(bad_words) != set():
            return True
        else:
            return False

