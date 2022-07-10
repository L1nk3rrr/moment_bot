import logging

from aiogram.utils import executor

#from tg_bot.handlers.admin import register_admin
from create_bot import dp, bot
from services.sqlite_db import sql_start

from handlers.general_handlers import register_general
from handlers.start import register_start
from handlers.share_emotions_handler import register_share_emotions
from handlers.day_analyze_handler import register_day_analyze
from handlers.last_handlers import register_last
from filters import AdminFilter
from filters.auth import Register


logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    # dp.setup_middleware(...)
    pass


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(Register)


def register_all_handlers(dp):
    # register_admin(dp)
    register_start(dp)
    register_general(dp)
    register_share_emotions(dp)
    register_day_analyze(dp)
    register_last(dp)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u"%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)
    if sql_start():
        logger.info("Database is ok")
    executor.start_polling(dp, skip_updates=True)



if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot Stopped")

