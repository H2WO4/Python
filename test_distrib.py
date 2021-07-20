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
d: Dict[int, float] = {}

num = (1, 7, 2)

for i in range(100000):
    w = round(normal(1, 6, 3, 4))
    x = round(normal(1, 7, 3, 4))
    y = round(normal(1, 8, 3, 4))
    z = round(normal(1, 9, 3, 4))
    a[w] = a.get(w, 0) +  0.001
    b[x] = b.get(x, 0) +  0.001
    c[y] = c.get(y, 0) +  0.001
    d[z] = d.get(z, 0) +  0.001

plot(sorted(a.keys()), [a[i] for i in sorted(a.keys())], "x-", label="2")
plot(sorted(b.keys()), [b[i] for i in sorted(b.keys())], "x-", label="3")
plot(sorted(c.keys()), [c[i] for i in sorted(c.keys())], "x-", label="4")
plot(sorted(d.keys()), [d[i] for i in sorted(d.keys())], "x-", label="5")
legend()
axis((None, None, 0, 50))
show()