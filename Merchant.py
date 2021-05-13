# Import
from __future__ import annotations
from functools import reduce
from math import inf
from typing import Callable, Dict, List, Literal, Tuple
from random import choices, gauss


# Normal distribution within bounds with automatic sigma
def normal(lowBound: float, highBound: float, mu: float, sigma: float) -> int:
    x = round(gauss(mu, (highBound - lowBound) / sigma))
    if lowBound <= x and x <= highBound:
        return x
    return normal(lowBound, highBound, mu, sigma)

def trim_dict(entry: Dict[str, int]) -> Dict[str, int]:
    return {i: entry[i] for i in entry if entry[i] != 0}

def combine_dicts(*entry: Dict[str, int]) -> Dict[str, int]:
    return trim_dict(reduce(lambda d1, d2: {i: d1.get(i, 0) + d2.get(i, 0) for i in (d1 | d2)}, entry))

def mul_dict(entry: Dict[str, int], times: int) -> Dict[str, int]:
    return {i: entry[i] * times for i in entry}


class Container:
    def __init__(self, name: str) -> None:
        self.name = name
        self.content: Dict[str, int] = {}
    
    def add(self, *other: Dict[str, int]) -> None:
        self.content = combine_dicts(self.content, *other)

    def can_sub(self, other: Dict[str, int]) -> bool:
        return all(self.content.get(i, inf) >= other[i] for i in other)

    def sub(self, other: Dict[str, int]) -> None:
        self.add(mul_dict(other, -1))

    def move(self, other: Container, items: Dict[str, int]) -> None:
        self.sub(items)
        other.add(items)

    def __str__(self) -> str:
        return "{}:\n".format(self.name) + "\n".join(["{} x{}".format(i, self.content[i]) for i in sorted(self.content.keys())])


class PoolGen:
    def __init__(self, entries: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.content = entries
    
    def add(self, entries: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.content |= entries

    def roll(self, times: int = 1) -> List[Dict[str, int]]: 
        return [{i: self.content[i][0](*self.content[i][1])} for i in choices([j for j in self.content], k=times)]

def equiPool(items: List[str], method: Callable[..., int], distribution: Tuple[float, ...]) -> PoolGen:
    return PoolGen({i: (method, distribution) for i in items})

def simiPool(items: Dict[str, Tuple[float, ...]], method: Callable[..., int]) -> PoolGen:
    return PoolGen({i: (method, items[i]) for i in items})


class ExchangeInterface:
    def __init__(self, name: str, content: List[Tuple[Dict[str, int], Dict[str, int]]]) -> None:
        self.name = name
        self.content = content
    
    def add(self, *content: Tuple[Dict[str, int], Dict[str, int]]) -> None:
        for i in content:
            self.content.append(i)

    def exchange(self, source: Container, destination: Container, index: int, times: int | Literal["max"] = 1) -> None:
        if times == "max": times = min([source.content[i] // self.content[index][0][i] for i in self.content[index][0]])

        if times > 0 and source.can_sub(mul_dict(self.content[index][0], times)):
            source.sub(mul_dict(self.content[index][0], times))
            destination.add(mul_dict(self.content[index][1], times))
        
        else: print("Insufficient ressources")

    def __str__(self) -> str:
        return "{}:\n".format(self.name) + "\n".join(["[{}] {} -> {}".format(i+1, ", ".join(["{} x{}".format(j, self.content[i][0][j]) for j in self.content[i][0]]), ", ".join(["{} x{}".format(j, self.content[i][1][j]) for j in self.content[i][1]])) for i in range(len(self.content))])


class MerchantInterface(ExchangeInterface):
    def __init__(self, name: str, content: List[Tuple[Dict[str, int], Dict[str, int]]]) -> None:
        self.name = name
        self.content = content
        self.inventory = Container(name + "'s Wares")
    
    def exchange(self, source: Container, destination: Container, index: int, times: int | Literal["max"] = 1) -> None:
        if times == "max": times = min(min([source.content.get(i, 0) // self.content[index][0][i] for i in self.content[index][0]]), min([self.inventory.content.get(i, 0) // self.content[index][1][i] for i in self.content[index][1]]))

        if times > 0 and source.can_sub(mul_dict(self.content[index][0], times)) and self.inventory.can_sub(mul_dict(self.content[index][1], times)):
            source.sub(mul_dict(self.content[index][0], times))
            self.inventory.sub(mul_dict(self.content[index][1], times))
            destination.add(mul_dict(self.content[index][1], times))
        
        else: print("Insufficient ressources")


class CollectionPoint:
    members: Dict[str, CollectionPoint] = {}

    def __init__(self, name: str, pool: PoolGen) -> None:
        CollectionPoint.members[name] = self

        self.name = name
        self.pool = pool


class Inventory:
    members: Dict[str, Inventory] = {}

    def __init__(self, name: str, container: Container) -> None:
        Inventory.members[name] = self

        self.name = name
        self.container = container


Bag = Container("Bag")
MoneyBag = Container("Money Bag")

Fruits = equiPool(["Apple", "Citrus", "Banana", "Orange", "Rawsberry"], normal, (2, 5, 3, 3))

FruitsBuyer = MerchantInterface("Fruits Buyer",
[
    ({"Apple": 5}, {"Gold": 4}),
    ({"Citrus": 5, "Banana": 3}, {"Gold": 5, "Copper": 5})
])
FruitsBuyer.inventory.add({"Gold": 10000, "Copper": 2000})


Self = Inventory("Self", Bag)
Orchard = CollectionPoint("Ochard", Fruits)


quitting = False
while not quitting:
    match input().split(" "):
        case ["collect", x, n]:
            Bag.add(*CollectionPoint.members[x].pool.roll(int(n)))

        case ["see", x]:
            print(Inventory.members[x].container)

        case ["pause"]:
            pass

        case ["quit"]:
            quitting = True