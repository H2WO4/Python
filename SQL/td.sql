SELECT titre FROM films WHERE score = (SELECT MAX(score) FROM films)

SELECT titre, nom FROM films, acteurs WHERE idActeur = idMetteurEnScene AND annee = 1983

SELECT titre, annee FROM films, casting WHERE idMetteurEnScene = (SELECT idActeur FROM acteurs WHERE nom = 'Alfred Hitchcock') ORDER BY annee

SELECT titre, annee FROM films AS F WHERE (SELECT idActeur FROM casting WHERE F.idFilm = idFilm) = (SELECT idActeur FROM acteurs WHERE nom = 'Sean Connery') AND (SELECT posCast FROM casting WHERE F.idFilm = idFilm) = 1 ORDER BY annee

SELECT titre, nom, annee FROM films AS F, acteurs WHERE idActeur = idMetteurEnScene AND (SELECT idActeur FROM casting WHERE F.idFilm = idFilm) = (SELECT idActeur FROM acteurs WHERE nom = 'Harrison Ford') AND (SELECT posCast FROM casting WHERE F.idFilm = idFilm) > 1 ORDER BY annee

SELECT nom FROM acteurs WHERE idActeur IN (SELECT idActeur FROM casting AS C, films AS F WHERE C.idActeur = idActeur AND F.idFilm = C.idFilm AND F.titre = 'Never Say Never Again')

SELECT nom FROM acteurs AS A WHERE (SELECT COUNT(idActeur) FROM casting AS C WHERE posCast = 1 AND C.idActeur = A.idActeur) >= 15

SELECT titre, (SELECT COUNT(idActeur) FROM casting AS C WHERE C.idFilm = F.idFilm) AS size FROM films AS F WHERE annee = 1999 ORDER BY size DESC

SELECT (SELECT nom FROM acteurs as A WHERE C.idActeur = A.idActeur) FROM casting AS C, casting as C2 WHERE C.idFilm = C2.idFilm AND C2.idActeur = (SELECT idActeur FROM acteurs as A WHERE A.nom = 'Arnold Schwarzenegger')