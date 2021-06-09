from random import shuffle

# On définit une fonction SelectionSort
# Cet algorithme trouve le minimum de la liste, et le place à la première position, il continue ensuite en ignorant le premier élément
# Cet algorithme, malgrès sa faible efficacité, prend toujours le même temps pour trier une liste de taille n
def SelectionSort(toSort):
    # On effectue une copie de la liste, pour éviter de changer la liste originelle
    toSortCopy = toSort.copy()

    # On répéte autant de fois qu'il y a d'éléments dans la liste
    for i in range(len(toSortCopy)):
        # On initialise le minimum de la liste au premier élément étudié
        minimumIndex = i

        # Pour chaque élément de la sous-liste étudiée
        for j in range(i+1, len(toSortCopy)):
            # Si l'élément est plus petit que notre minimum présumé
            if toSortCopy[j] < toSortCopy[minimumIndex]:
                # Alors, c'est notre nouveau minimum présumé
                minimumIndex = j

        # On fini cet itération par échanger le minimum avec le premier élément de la sous-liste étudiée
        toSortCopy[i], toSortCopy[minimumIndex] = toSortCopy[minimumIndex], toSortCopy[i]
    
    # On retourne la liste triée
    return toSortCopy

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
print(SelectionSort(liste))