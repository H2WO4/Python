SELECT COUNT(*) FROM films WHERE idrealisateur = 11

SELECT nom, (SELECT COUNT(*) FROM films AS F WHERE F.idrealisateur = R.id) FROM realisateurs AS R ORDER BY nom

SELECT titre, id, (SELECT COUNT(*) FROM distributions AS D WHERE D.idfilm = F.id) FROM films AS F

SELECT nom, id FROM acteurs AS A WHERE (SELECT COUNT(*) FROM distributions AS D WHERE D.idacteur = A.id) >= 3

SELECT nom, id FROM realisateurs AS R WHERE (SELECT COUNT(*) FROM films AS F WHERE F.idrealisateur = R.id) = (SELECT MAX((SELECT COUNT(*) FROM films as F2 WHERE F2.idrealisateur = R2.id)) FROM realisateurs as R2)

SELECT nom, id FROM acteurs AS A WHERE (SELECT COUNT(*) FROM films AS F WHERE F.idrealisateur = 287 AND F.annee > 1940) = (SELECT COUNT(*) FROM distributions AS D WHERE D.idacteur = A.id AND D.idfilm IN (SELECT id FROM films AS F WHERE F.idrealisateur = 287 AND F.annee > 1940))

SELECT nom, id FROM acteurs AS A WHERE (SELECT idfilm FROM distributions AS D WHERE D.idacteur = 552 GROUP BY D.idfilm) IN (SELECT idfilm FROM distributions AS D WHERE D.idacteur = A.id  GROUP BY D.idfilm)

SELECT nom, id, (SELECT COUNT(*) FROM distributions AS D JOIN films AS F ON D.idfilm = F.id WHERE A.id = D.idacteur AND (SELECT COUNT(*) FROM realisateurs AS R WHERE R.id = F.idrealisateur) >= 2) FROM acteurs AS A
