from math import factorial
from itertools import accumulate

n = int(input("Entrez un nombre : "))

print("Somme de 1 à n : {}".format([*accumulate(range(n+1))][-1]))
print("Produit de 1 à n : {}".format(factorial(n)))