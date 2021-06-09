import sqlite3 as sql
import os
import re

database = os.path.join(os.getcwd(), "cinema.sql")

def regexp(expr: str, item: str):
    return re.match(expr, item, flags=re.I) is not None

with sql.connect(database) as db:
    db.create_function("REGEXP", 2, regexp)
    cur = db.cursor()

    # cur.execute("SELECT titre FROM films WHERE score = (SELECT MAX(score) FROM films)")
    # cur.execute("SELECT titre, nom FROM films, acteurs WHERE idActeur = idMetteurEnScene AND annee = 1983")
    # cur.execute("SELECT titre, annee FROM films, casting WHERE idMetteurEnScene = (SELECT idActeur FROM acteurs WHERE nom = 'Alfred Hitchcock') ORDER BY annee")
    # cur.execute("SELECT titre, annee FROM films AS F WHERE (SELECT idActeur FROM casting WHERE F.idFilm = idFilm) = (SELECT idActeur FROM acteurs WHERE nom = 'Sean Connery') AND (SELECT posCast FROM casting WHERE F.idFilm = idFilm) = 1 ORDER BY annee")
    # cur.execute("SELECT titre, nom, annee FROM films AS F, acteurs WHERE idActeur = idMetteurEnScene AND (SELECT idActeur FROM casting WHERE F.idFilm = idFilm) = (SELECT idActeur FROM acteurs WHERE nom = 'Harrison Ford') AND (SELECT posCast FROM casting WHERE F.idFilm = idFilm) > 1 ORDER BY annee")
    # cur.execute("SELECT nom FROM acteurs WHERE idActeur IN (SELECT idActeur FROM casting AS C, films AS F WHERE C.idActeur = idActeur AND F.idFilm = C.idFilm AND F.titre = 'Never Say Never Again')")
    # cur.execute("SELECT nom FROM acteurs AS A WHERE (SELECT COUNT(idActeur) FROM casting AS C WHERE posCast = 1 AND C.idActeur = A.idActeur) >= 15")
    # cur.execute("SELECT titre, (SELECT COUNT(idActeur) FROM casting AS C WHERE C.idFilm = F.idFilm) AS size FROM films AS F WHERE annee = 1999 ORDER BY size DESC")
    # cur.execute("SELECT (SELECT nom FROM acteurs as A WHERE C.idActeur = A.idActeur) FROM casting AS C, casting as C2 WHERE C.idFilm = C2.idFilm AND C2.idActeur = (SELECT idActeur FROM acteurs as A WHERE A.nom = 'Arnold Schwarzenegger')")

    for i in cur:
        print("{}: {}, {}".format(i[0], i[1], i[2]))