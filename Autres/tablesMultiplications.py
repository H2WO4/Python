n = int(input("Quelle table voulait vous afficher : "))

print()
for i in range(11):
    print("{} × {} = {}".format(i, n, i*n))