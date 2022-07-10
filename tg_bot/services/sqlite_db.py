import sqlite3 as sq

def sql_start():
    global base, cr
    base = sq.connect("moment.db")
    cr = base.cursor()
    base.execute("CREATE TABLE IF NOT EXISTS moment_users(tg_id TEXT PRIMARY KEY, name VARCHAR(60))")
    base.commit()
    return True


async def new_user(tg_id, name):
    with sq.connect("moment.db") as base_1:
        cr_1 = base_1.cursor()
        cr_1.execute("INSERT INTO moment_users VALUES (?, ?)", (tg_id, name))
        base_1.commit()


async def get_user_name(tg_id):
    with sq.connect("moment.db") as base_1:
        cr_1 = base_1.cursor()
        cr_1.execute(f"SELECT name FROM moment_users WHERE tg_id = {tg_id}")
        res = cr_1.fetchone()
        return res or False