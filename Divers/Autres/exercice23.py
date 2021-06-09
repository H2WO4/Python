""" Recursive Function """

def getParent(sequence, units, number):
    """ Finds all of a number's parents """

    # On parcours toute la liste
    for j in range(len(sequence)):
        # Pour chaque nombre supérieur à 1, on lui retire n, compris entre n et j - 1
        for i in range(1, (sequence[j] // 2) + 1):
            # On place n dans la liste, à gauche de j
            sequenceCopy = sequence.copy()
            sequenceCopy[j] -= i
            sequenceCopy.append(i)

            # On fait une première récursion
            if not getParent(sequenceCopy, units, number):
                return False

            # On place n dans la liste, à droite de j
            sequenceCopy2 = sequence.copy()
            sequenceCopy2[j] -= i
            sequenceCopy2.insert(j-1, i)

            # On fait une deuxième récursion
            if not getParent(sequenceCopy2, units, number):
                return False

    # On teste si la sequence en question est divisible par le nombre actuel
    if int("".join([str(j) for j in sequence]) + str(units)) % number == 0:
        return True
    return False



""" Main loop """

# Definition du liste pour l'ensemble de sortie
n = []

# Boucle testant tout les cas
for i in range(10, 100):
    # On sépare chiffre des unités et des dizaines
    units = i % 10
    tens = (i - units) // 10

    # On lance la fonction récursive
    parentsDivisibility = getParent([tens], units, i)

    # Si aucun des nombres parents n'a renvoyé False, alors tous sont divisibles par i
    if parentsDivisibility:
        n.append(i)

# On affiche la réponse
print(n)