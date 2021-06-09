from random import shuffle
from math import inf

def onePerOne(toSort):
    new = []
    toSortCopy = toSort.copy()

    for i in toSortCopy:
        low = inf
        index = 0

        for j in range(len(toSort)):
            if low > toSort[j]:
                low = toSort[j]

                index = j

        new.append(toSort.pop(index))
    
    return new

def swapSort(toSort):
    finished = False

    while not finished:
        finished = True

        for i in range(len(toSort) - 1):
            if toSort[i+1] < toSort[i]:
                toSort[i+1], toSort[i] = toSort[i], toSort[i+1]

                finished = False
    
    return toSort


listToSort = list(range(1, 201))
shuffle(listToSort)

listToSortRepeat = list(range(1, 101))
listToSortRepeat.extend(list(range(1,101)))
shuffle(listToSortRepeat)

print(swapSort(listToSort))
print(swapSort(listToSortRepeat))