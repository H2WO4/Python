from random import shuffle

# On définit une fonction StalinSort
# Cet algorithme fonctionne en supprimant tout les éléments non conformes (d'où le nom)
# Ceci n'est pas un véritable alogrithme de tri, car la liste n'est pas conserver entiérement.
def StalinSort(toSort):
    # On effectue une copie de la liste, pour éviter de changer la liste originelle
    toSortCopy = toSort.copy()

    # On initialise la valeur précédente à 0, car la valeur précédente n'est pas forcément la valeur i-1
    previous = 0
    # On initialise une liste vide des éléments à supprimer
    toDelete = []
    # On parcours la liste à trier
    for i in range(len(toSortCopy)):
        # Si l'élément est conforme, il devient le nouveau "modéle"
        if previous <= toSortCopy[i]:
            previous = toSortCopy[i]
        # Sinon, il est mis sur la liste de suppresion
        else:
            toDelete.append(i)
    
    # On inverse la liste, afin que la suppresion des éléments ne perturbe pas la place des autres éléments
    toDelete.reverse()
    # On supprime tout les éléments non-conformes
    for i in toDelete:
        del toSortCopy[i]
    
    # On retourne la liste "triée"
    return toSortCopy

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
print(StalinSort(liste))