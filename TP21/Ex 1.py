from numpy import cos, linspace, pi
from matplotlib.pyplot import plot, show, title

x = linspace(-pi, pi, 361)

def Ep(y):
    return 1 - cos(y)

def Ec(y):
    return (y ** 2) / 2


plot(x, Ep(x))
# plot(x, Ec(x))
title("Allure de la courbe de Ep")
show()