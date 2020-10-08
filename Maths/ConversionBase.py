def tenToBinary(value10):
    value2 = ""
    n = 0
    while 2**n <= value10:
        n += 1 
    
    for i in range(0, n).__reversed__():
        if value10 - 2**i >= 0:
            value10 -= 2**i
            value2 += "1"
        else:
            value2 += "0"

    return int(value2)

def binaryToDecimal(value2):
    value2 = str(value2)
    n = len(value2) - 1
    value10 = 0
    for i in value2:
        if i == "1":
            value10 += 2**n
        n -= 1
    
    return value10

def binaryToHexadecimal(value2):
    value2 = str(value2)


print(tenToBinary(14))

print(binaryToDecimal(1011))
