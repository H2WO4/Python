from random import shuffle

# On définit une fonction MergeSort
# Cet algorithme de tri est recursif, il fait donc appel à lui même dans la définition de sa fonction
# Il fonctionne en séparant la liste en groupes de 1, puis en triant ces groupes pour les joindres à nouveau
# L'un des algorithme les plus rapide, seul probléme, c'est celui qui prend le plus de place sur la RAM pendant son execution
def MergeSort(toSort):
    # On verifie que la liste d'entrée contient au moins deux éléments
    if len(toSort) > 1:
        # On prend le millieu de la liste, dans le cas de n impaire, la liste de gauche sera plus grande
        midPoint = round(len(toSort)/2)
        # On prend les deux listes correspondants à la séparation en deux
        list1 = toSort[:midPoint]
        list2 = toSort[midPoint:]

        # On commence la reccursion, afin de trier ces deux listes suivant un MergeSort
        list1 = MergeSort(list1)
        list2 = MergeSort(list2)
        # Les deux listes sont donc maintenant triées indépendamment les unes des autres

        # On définie une liste vide pour trier les deux listes entre elles
        output = []
        # Pour tout les éléments des deux listes
        for _ in range(len(list1) + len(list2)):
            # Si la première liste est vide, alors on prend une valeur dans la deuxième
            if len(list1) < 1:
                output.append(list2[0])
                del list2[0]
            # Si la deuxième liste est vide, alors on prend une valeur dans la première
            elif len(list2) < 1:
                output.append(list1[0])
                del list1[0]

            # Si le premier élément de la première liste est plus petit que le premier élément de la deuxième liste
            elif list1[0] < list2[0]:
                # Alors on ajoute cette élément à la liste de sortie
                output.append(list1[0])
                # Et on le supprime de sa liste
                del list1[0]
            # Sinon, cela signifie que c'est le premier élément de la deuxième liste qui est plus petit
            else:
                # Donc on l'ajoute à la liste de sortie
                output.append(list2[0])
                # Et on le supprime de sa liste
                del list2[0]
        
        # On fini par retourner la liste de sortie
        return output
    
    # Sinon, on retourne l'entrée sans rien faire, afin d'éviter d'avoir une recursion infinie
    return toSort

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
print(MergeSort(liste))