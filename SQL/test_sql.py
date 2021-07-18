import sqlite3 as sql
import os
import re

database = os.path.join(os.getcwd(), "convertcsv.sql")

def regexp(expr: str, item: str):
    return re.match(expr, item, flags=re.I) is not None

with sql.connect(database) as db:
    db.create_function("REGEXP", 2, regexp)
    cur = db.cursor()

    cur.execute("SELECT * FROM mytable")
    
    for i in cur:
        print("{}".format(i[0]))