from random import shuffle

# On définit une fonction InsertionSort
# Cet algorithme créer une nouvelle liste, et place aux bonnes places les éléments de la liste mère, un à un
# Pas très efficace pour des listes entièrement aléatoires, mais l'un des plus efficace pour les listes presque rangées
def InsertionSort(toSort):
    # On commence par créer la liste secondaire, et à l'initialiser à la première valeur de la liste mère
    output = [toSort[0]]

    # Pour chaque élément de la liste (à part le premier, déjà trié)
    for i in toSort[1:]:
        # On commence à se placer à la fin de la liste secondaire
        n = len(output)
        # Puis, on compare notre élément actuel avec chacun des éléments de la liste, jusqu'a ce que l'élément de la liste soit plus petit
        while (i < output[n-1]) and (n > 0):
            n -= 1
        # On place donc notre nouvel élément après cet élément
        output.insert(n, i)
    
    # On retourne la liste
    return output

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
print(InsertionSort(liste))