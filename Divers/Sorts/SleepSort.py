# Importation des modules nécessaires
from time import sleep
from threading import Timer
from random import shuffle

# Définition de la fonction
# Cette fonction marche car tout les éléments 1 sont ajoutés à la liste résultat après 1s, tout les éléments 2 après 2s ... (pour une précision de 1)
# Vu que l'éxecution est faite en parralèle, les éléments plus petits arrivent en premiers dans la liste, et donc prennent les premières places
# Algorithme de tri purement humoristique, à ne pas utiliser dans un programme sérieux ! (Surtout qu'il n'est pas 100% précis ...)
def SleepSort(toSort, precision):
    # Définition d'une liste résultat vide
    result = []
    # Définition d'un fonction auxiliaire à la fonction
    def AppendSleep(number):
        # Cet fonction ajoute la valeur qu'on lui fourni à la fin de la liste résultat
        result.append(number)
    # Définition d'une variable maximum, initialisé à 0
    maximum = 0
    # Pour chaque élément de la liste
    for i in toSort:
        # Si cet élément est plus grand que le maximum, alors il devient le nouveau maximum
        if i > maximum: maximum = i
        # On met en place un Timer tel que dans i * precision secondes, on effectue la fonction AppendSleep avec i en paramètre
        Timer(i * precision, AppendSleep, [i]).start()
    
    # On attends un peu plus que le maximum de la liste secondes
    sleep((maximum+1) * precision)
    # On retourne le résultat
    return result

# On teste la fonction
liste = [*range(100)]
shuffle(liste)
print(liste)
print(SleepSort(liste, 0.1)) # En dessous de 0.1, il y a des chances qu'il y ai des erreures
print(SleepSort(liste, 0.01)) # Mais cela peut servir à faire des listes presque triées