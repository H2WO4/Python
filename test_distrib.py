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

for i in range(100000):
    x = round(normal(1, 4, 1, 2))
    y = round(normal(1, 4, 1, 3))
    z = round(normal(1, 4, 1, 4))
    a[x] = a.get(x, 0) +  0.001
    b[y] = b.get(y, 0) +  0.001
    c[z] = c.get(z, 0) +  0.001

plot(sorted(a.keys()), [a[i] for i in sorted(a.keys())], "x-", label="2")
plot(sorted(b.keys()), [b[i] for i in sorted(b.keys())], "x-", label="3")
plot(sorted(c.keys()), [c[i] for i in sorted(c.keys())], "x-", label="4")
legend()
axis((None, None, 0, 100))
show()