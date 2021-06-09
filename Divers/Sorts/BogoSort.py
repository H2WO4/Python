# On importe le module nécessaire
from random import shuffle

# On définie un fonction BogoSort
# Cet algorithme marche de la manière suivante, si la liste n'est pas triée, on la mélange
# Bien évidement, cet algoithme est une blague, et prend généralement n! itérations, avec n la taille de la liste
def BogoSort(toSort):

    # On défini une fonction auxiliaire IsSorted
    def IsSorted(inList):
        # Si la liste est trié, son minimum est le premier nombre
        minimum = inList[0]
        # On teste pour chaque élément de la liste
        for i in inList[1:]:
            # Si il est inférieur au minimum, alors la liste n'est pas triée
            if i < minimum:
                # Donc on sort de la fonction
                return False
        
            # Le nombre que l'on vient de tester est donc le nouveau minimum
            minimum = i
        
        # Si il n'y a aucun problème, la liste est donc triée
        return True

    # On effectue une copie de la liste
    toSortCopy = toSort.copy()
    
    # On se place dans une boucle infinie
    while True:
        # Si la liste est triée
        if IsSorted(toSortCopy):
            # Alors on retourne la liste
            return toSortCopy
        
        # Sinon, on mélange la liste
        shuffle(toSortCopy)

# On teste la fonction
liste = [*range(9)] # Ce serait suicidaire de trier une liste de 100 éléments, donc on se limitera à 8, car même 9 c'est trop
shuffle(liste)
print(liste)
print(BogoSort(liste))