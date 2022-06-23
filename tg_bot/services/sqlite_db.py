import sqlite3 as sq

def sql_start():
    global base, cr
    base = sq.connect("moment.db")
    cr = base.cursor()
    cr.execute("""CREATE TABLE IF NOT EXISTS""")