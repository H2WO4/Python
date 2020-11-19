""" Recursive Function """

def totalValue(n):
    """ Calculate the sum of all of a number's digits """
    output = 0
    for i in str(n):
        output += int(i)
    return output

def getParent(sequence):
    """ Finds all of a number's parents """
    output = [sequence.copy()]

    if len(sequence) == (totalValue(int("".join([str(i) for i in sequence]))) - 1):
        return output

    for j in range(len(sequence)):
        for i in range(1, (sequence[j] // 2) + 1):
            sequenceCopy = sequence.copy()
            sequenceCopy[j] -= i
            sequenceCopy.insert(j+1, i)
            output.extend(getParent(sequenceCopy))

            sequenceCopy2 = sequence.copy()
            sequenceCopy2[j] -= i
            sequenceCopy2.insert(j-1, i)
            output.extend(getParent(sequenceCopy2))

    return output



""" Main loop """

n = []

for i in range(10, 99):
    units = i % 10
    tens = (i - units) // 10
    parentList = getParent([tens])

    toPop = []
    parents = []

    for k in range(len(parentList)):
        for j in range(len(parentList)):
            if parentList[k] == parentList[j] and (k < j) :
                if j not in toPop:
                    toPop.append(j)
    
    toPop.sort()
    toPop.reverse()
    for k in toPop:
        del parentList[k]

    for k in range(len(parentList)):
        parents.append(int("".join([str(j) for j in parentList[k]]) + str(units)))
    
    value = ""

    for k in range(tens):
        value += "1"
    value += str(units)
    parents.append(int(value))

    if all([(k % i) == 0 for k in parents]):
        print(i)