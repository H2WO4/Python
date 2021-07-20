SELECT SUM(R.quantite) FROM recoltes AS R WHERE R.nvin = 12

SELECT V.cru, SUM(R.quantite) FROM vins AS V JOIN recoltes AS R ON V.num = R.nvin GROUP BY V.cru ORDER BY V.cru

SELECT V.num, V.cru, SUM((SELECT COUNT(DISTINCT R.nprod) from recoltes AS R WHERE R.nvin = V.num)) FROM vins AS V GROUP BY V.cru

SELECT P.nom, P.prenom FROM producteurs AS P WHERE (SELECT COUNT(DISTINCT R.nvin) FROM recoltes AS R WHERE R.nprod = P.num) >= 3

SELECT P.nom, P.prenom, (SELECT SUM(R.quantite) AS total FROM vins AS V JOIN recoltes AS R ON V.num = R.nvin AND R.nprod = P.num) AS crues FROM producteurs AS P WHERE crues >= 1