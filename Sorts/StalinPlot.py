from random import shuffle
from matplotlib.pyplot import plot, show

def StalinSort(toSort):
    toSortCopy = toSort.copy()
    previous = 0
    toDelete = []
    for i in range(len(toSortCopy)):
        if previous <= toSortCopy[i]:
            previous = toSortCopy[i]
        else:
            toDelete.append(i)
    toDelete.reverse()
    for i in toDelete:
        del toSortCopy[i]
    return toSortCopy

LengthListStalin = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
ListLengthStalin = []
for j in LengthListStalin:
    LengthStalin = 0
    for i in range(10000):
        liste = [*range(j)]
        shuffle(liste)
        LengthStalin += len(StalinSort(liste))

    ListLengthStalin.append(LengthStalin / 10000)

plot(LengthListStalin, ListLengthStalin)
show()