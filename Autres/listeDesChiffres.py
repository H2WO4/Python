def chiffre(x, list):
    list.append(x % 10)

    if x >= 10:
        return chiffre(x // 10, list)
    return list

n = int(input())

chiffres = chiffre(n, [])

chiffres.reverse()
print(chiffres)

print("Le nombre se trouve entre 2^{} et 2^{}".format(len(chiffres), len(chiffres) - 1))