from random import gauss
from typing import Dict
from matplotlib.pyplot import axis, legend, plot, show

def normal(lowBound: float, highBound: float, mu: float, sigma: float) -> int:
    x = round(gauss(mu, (highBound - lowBound) / sigma))
    if lowBound <= x <= highBound:
        return x
    return normal(lowBound, highBound, mu, sigma)

a: Dict[int, float] = {}
b: Dict[int, float] = {}
c: Dict[int, float] = {}

num = (1, 6, 2)

for i in range(100000):
    x = round(normal(*num, 2))
    y = round(normal(*num, 3))
    z = round(normal(*num, 4))
    a[x] = a.get(x, 0) +  0.001
    b[y] = b.get(y, 0) +  0.001
    c[z] = c.get(z, 0) +  0.001

plot(sorted(a.keys()), [a[i] for i in sorted(a.keys())], "x-", label="2")
plot(sorted(b.keys()), [b[i] for i in sorted(b.keys())], "x-", label="3")
plot(sorted(c.keys()), [c[i] for i in sorted(c.keys())], "x-", label="4")
legend()
axis((None, None, 0, 50))
show()