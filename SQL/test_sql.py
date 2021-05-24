from sqlite3 import connect
import os

database = os.path.join(os.getcwd(), "SQL\\AnimeList.sql")

with connect(database) as db:
    cur = db.cursor()

    cur.execute("SELECT * FROM anime")