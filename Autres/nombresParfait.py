from math import isqrt

x = int(input("Entrez un nombre : "))

for n in  range(6, x):
    diviseurs = [1]

    for i in range(2, 1 + isqrt(n - 1)):
        if n % i == 0:
            diviseurs.append(i)
            diviseurs.append(n//i)

    totalSum = 0
    for i in diviseurs:
        totalSum += i

    if totalSum == n:
        print("{} est parfait".format(n))