# Import
from math import inf
from typing import Callable, Dict, List, Tuple
from random import choices, gauss


# Normal distribution within bounds with automatic sigma
def normal(lowBound: float, highBound: float, mu: float, sigma: float) -> int:
    x = round(gauss(mu, (highBound - lowBound) / sigma))
    if lowBound <= x and x <= highBound:
        return x
    return normal(lowBound, highBound, mu, sigma)

def combine_dicts(*entry: Dict[str, int]) -> Dict[str, int]:
    output: Dict[str, int] = {}
    for i in entry:
        for j in i:
            output[j] = output.get(j, 0) + i[j]
    return output


class Container:
    def __init__(self, name: str) -> None:
        self.name = name
        self.content: Dict[str, int] = {}
    
    def add(self, *other: Dict[str, int]) -> None:
        for i in other:
            for j in i:
                self.content[j] = self.content.get(j, 0) + i[j]

    def can_sub(self, other: Dict[str, int]) -> bool:
        return all(self.content.get(i, inf) >= other[i] for i in other)

    def sub(self, other: Dict[str, int]) -> None:
        for i in other:
            self.content[i] -= other[i]


    def move(self, other: Container, item: Dict[str, int]) -> None:
        self.sub(item)
        other.add(item)

    def __str__(self) -> str: return "{}:\n".format(self.name) + "\n".join(["{} x{}".format(i, self.content[i]) for i in sorted(self.content.keys())])


class PoolGen:
    def __init__(self, results: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.results = results

    def roll(self, times: int = 1) -> List[Dict[str, int]]: 
        return [{i: self.results[i][0](*self.results[i][1])} for i in choices([j for j in self.results], k=times)]

def equiPool(items: List[str], distribution: Tuple[float, ...], method: Callable[..., int]) -> PoolGen:
    return PoolGen({i: (method, distribution) for i in items})

def simiPool(items: Dict[str, Tuple[float, ...]], method: Callable[..., int]) -> PoolGen:
    return PoolGen({i: (method, items[i]) for i in items})



class 




Bag = Container("Bag")

Fruits = equiPool(["Apple", "Orange", "Banana", "Rawsberry", "Citrus"], (2, 5, 3, 3), normal)

