# Import
from typing import Callable
from random import choices, gauss, randint


# Normal distribution within bounds with automatic sigma
def normal(lowBound: float, highBound: float, mu: float, sigma: float) -> int:
    x = round(gauss(mu, (highBound - lowBound) / sigma))
    if lowBound <= x and x <= highBound:
        return x
    return normal(mu, sigma, lowBound, highBound)



class Item:

    def __init__(self, name: str, amount: int = 1) -> None:
        self.name = name
        self.amount = amount

    def __eq__(self, other: Item): return self.name == other.name

    def __str__(self) -> str: return "{} ×{}".format(self.name, self.amount)


class Inventory:

    def __init__(self, name: str) -> None:
        self.name = name
        self.content: list[Item] = []
    
    def add(self, *other: Item) -> None:
        for i in other:
            for j in self.content:
                if j == i:
                    j.amount += i.amount
                    break
            else:
                self.content.append(i)
    
    def __str__(self) -> str: return "{}:\n".format(self.name) + "\n".join([str(i) for i in self.content])

    def sort(self) -> None: self.content.sort(key=str)

    def move(self, other: Inventory, item, amount: int = 1) -> None:
        pass


class PoolGen:

    def __init__(self, results: dict[str, tuple[float, ...]], method: Callable[..., int]) -> None:
        self.results = results
        self.method = method
    
    def roll(self, times: int = 1) -> list[Item]:
        return [Item(i, self.method(*self.results[i])) for i in choices([j for j in self.results], k=times)]


def equiPool(items: list[str], distribution: tuple[float, ...], method: Callable[..., int]) -> PoolGen:
    results = {}
    for i in items:
        results[i] = distribution
    return PoolGen(results, method)




A = Inventory("Bag")

Fruits = equiPool(["Apple", "Orange", "Banana", "Rawsbery", "Citrus"], (2, 5, 3, 3), normal)
A.add(*Fruits.roll(100))
A.sort()

print(A)