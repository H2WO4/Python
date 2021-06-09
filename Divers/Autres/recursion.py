def f(x, n):
    if n == 0:
        return x
    return (2 * f(x, n - 1) + 1) / (f(x, n - 1) + 2)

for i in range(10):
    print(f(2, i))

print(f(2, 99))