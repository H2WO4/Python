# Importation de la libairie pypng
from png import Reader, Writer

# Prend l'image d'entrée
textImage = input("Which image do you want to modify? : ")

# Formate les données de l'images afin de ne garder que le nécéssaire
image = Reader("{}.png".format(textImage))
i = image.read()
i = list(i[2])

# Initialise les listes vides
n = 0
outputR = []
outputG = []
outputB = []
outputC = []
outputM = []
outputY = []

""" Boucle principale parcourant l'image """

# Gère la présence ou l'absence de channel de couleur alpha
m = 3
if len(i) > (image.width * 3):
    m = 4

for k in i:
    # Parcours les lignes de l'image

    outputR.append([])
    outputG.append([])
    outputB.append([])
    outputM.append([])
    outputY.append([])
    outputC.append([])

    j = 0
    for l in k:
        # Parcours les colonnes de l'images

        # Regarde, par rraport à l'index, quel channel est observé et que faire
        if j%m == 0:
            outputR[n].append(l)
            outputG[n].append(0)
            outputB[n].append(0)
            outputM[n].append(l)
            outputY[n].append(l)
            outputC[n].append(0)

        elif j%m == 1:
            outputR[n].append(0)
            outputG[n].append(l)
            outputB[n].append(0)
            outputM[n].append(l)
            outputY[n].append(0)
            outputC[n].append(l)

        elif j%m == 2:
            outputR[n].append(0)
            outputG[n].append(0)
            outputB[n].append(l)
            outputM[n].append(0)
            outputY[n].append(l)
            outputC[n].append(l)

        if j%m == 3:
            outputR[n].append(l)
            outputG[n].append(l)
            outputB[n].append(l)
            outputM[n].append(l)
            outputY[n].append(l)
            outputC[n].append(l)

        j += 1
    
    n += 1

# Prépare l'objet Writer pour créer les nouvelles images
w = Writer(image.width, image.height, greyscale=False)

# Créer chacune des nouvelles images
f = open("{}R.png".format(textImage), "wb")
w.write(f, outputR)

f = open("{}B.png".format(textImage), "wb")
w.write(f, outputB)

f = open("{}G.png".format(textImage), "wb")
w.write(f, outputG)

f = open("{}M.png".format(textImage), "wb")
w.write(f, outputM)

f = open("{}Y.png".format(textImage), "wb")
w.write(f, outputY)

f = open("{}C.png".format(textImage), "wb")
w.write(f, outputC)

print("Séparation RGB complète")