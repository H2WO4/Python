from typing import Callable, Generator
from random import randint

double = lambda a: a*2
almostIncr = lambda a: a + randint(0, 1)

def funcRange(func: Callable, start: int, stop: int) -> Generator[int, None, None]:
    a = start
    while a < stop:
        yield a
        a = func(a)

def diverging_count(stop: int):
    a, b = 0, 0
    while a < stop:
        yield a,b
        a, b = a+1, b-1

for i, j in diverging_count(30):
    print(i, j)