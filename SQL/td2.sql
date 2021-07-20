SELECT * FROM Chasseurs WHERE prenom = "James"

SELECT SUM(population) FROM Quartiers

SELECT * FROM Fantomes WHERE dangerosite >= 50 ORDER BY dangerosite DESC

-- Un point (x, y) appartient à un quartier (xmin, ymin), (ymin, ymax) ssi xmin <= x <= xmax et ymin <= y <= ymax

SELECT C.* FROM Chasseurs AS C, Quartiers as Q WHERE Q.nom = "Manhattan" AND x_min <= x AND x <= x_max AND y_min <= y AND y <= y_max

SELECT id_quartier, COUNT(*) FROM Chasseurs GROUP BY id_quartier

SELECT * FROM Chasseurs WHERE id_quartier = 1 ORDER BY x*x+y*y ASC

SELECT COUNT(*) FROM Films WHERE idrealisateur = 11

SELECT R.nom, COUNT(SELECT * FROM Films WHERE idrealisateur = R.id) FROM Realisateurs AS R ORDER BY R.nom ASC

