from random import shuffle

# On définit une fonction BubbleSort
# Cet algorithme marche en comparant les éléments voisins deux à deux et en échangeant leurs places si besoin
# Cet type de tri possède une bonne efficacité et est constant. Il trie aussi bien petite et grandes listes
def BubbleSort(toSort):
    # On effectue une copie de la liste, pour éviter de changer la liste originelle
    toSortCopy = toSort.copy()

    # On répéte autant de fois qu'il y a d'éléments dans la liste
    for i in range(len(toSortCopy)):
        # On fait l'hypothèse que la liste est triée
        finished = True

        # On parcours la liste, à l'exception du premier élément, car on compare des paires, et des i derniers, car on est garanti qu'ils sont rangés
        for j in range(1, len(toSortCopy) - i):
            # Si une paire d'élément n'est pas rangée
            if toSortCopy[j] < toSortCopy[j-1]:
                # On utilise un double assignement pour echanger leurs places
                toSortCopy[j], toSortCopy[j-1] = toSortCopy[j-1], toSortCopy[j]
                # L'hypothèse était donc fausse
                finished = False

        # Mais si l'hypothèse était vraie, on retourne la liste maintenant    
        if finished:
            return toSortCopy
    
    # On retourne la liste triée
    return toSortCopy

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
print(BubbleSort(liste))