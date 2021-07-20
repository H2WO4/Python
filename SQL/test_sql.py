import sqlite3 as sql
import os

database = os.path.join(os.getcwd(), "SQL\\vins.sql")

with sql.connect(database) as db:
    cur = db.cursor()

    cur.execute("SELECT P.nom, P.prenom FROM producteurs AS P WHERE (SELECT COUNT(DISTINCT R.nvin) FROM recoltes AS R WHERE R.nprod = P.num) >= 3")    

    for i in cur:
        print("{}, {}".format(i[0], i[1]))