# Import
from functools import reduce
from math import inf
from typing import Callable, Dict, List, Literal, Tuple
from random import choices, gauss

Items = Dict[str, int]


# Normal distribution within bounds with automatic sigma
def normal(lowBound: float, highBound: float, mu: float, sigma: float) -> int:
    x = round(gauss(mu, (highBound - lowBound) / sigma))
    if lowBound <= x and x <= highBound:
        return x
    return normal(lowBound, highBound, mu, sigma)

def combine_dicts(*entry: Items) -> Items:
    return reduce(lambda d1, d2: {i: d1.get(i, 0) + d2.get(i, 0) for i in d1 | d2}, entry)


class Container:
    def __init__(self, name: str) -> None:
        self.name = name
        self.content: Items = {}
    
    def add(self, *other: Items) -> None:
        self.content = combine_dicts(self.content, *other)

    def can_sub(self, other: Items) -> bool:
        return all(self.content.get(i, inf) >= other[i] for i in other)

    def sub(self, other: Items) -> None:
        for i in other:
            self.content[i] -= other[i]

    def move(self, other: Container, items: Items) -> None:
        self.sub(items)
        other.add(items)

    def __str__(self) -> str:
        return "{}:\n".format(self.name) + "\n".join(["{} x{}".format(i, self.content[i]) for i in sorted(self.content.keys())])


class PoolGen:
    def __init__(self, entries: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.content = entries
    
    def add(self, entries: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.content |= entries

    def roll(self, times: int = 1) -> List[Items]: 
        return [{i: self.content[i][0](*self.content[i][1])} for i in choices([j for j in self.content], k=times)]

def equiPool(items: List[str], distribution: Tuple[float, ...], method: Callable[..., int]) -> PoolGen:
    return PoolGen({i: (method, distribution) for i in items})

def simiPool(items: Dict[str, Tuple[float, ...]], method: Callable[..., int]) -> PoolGen:
    return PoolGen({i: (method, items[i]) for i in items})


class ExchangeInterface:
    def __init__(self, name: str, content: List[Tuple[Items, Items]]) -> None:
        self.name = name
        self.content = content
    
    def add(self, *content: Tuple[Items, Items]) -> None:
        for i in content:
            self.content.append(i)

    def exchange(self, source: Container, destination: Container, index: int, times: int | Literal["max"] = 1) -> None:
        if times == "max": times = min([source.content[i] // self.content[index][0][i] for i in self.content[index][0]])

        if source.can_sub({i: self.content[index][0][i] * times for i in self.content[index][0]}) and times > 0:
            source.sub({i: self.content[index][0][i] * times for i in self.content[index][0]})
            destination.add({i: self.content[index][1][i] * times for i in self.content[index][1]})
        
        else: print("Insufficient ressources")

    def __str__(self) -> str:
        return "{}:\n".format(self.name) + "\n".join(["[{}] {} -> {}".format(i+1, ", ".join(["{} x{}".format(j, self.content[i][0][j]) for j in self.content[i][0]]), ", ".join(["{} x{}".format(j, self.content[i][1][j]) for j in self.content[i][1]])) for i in range(len(self.content))])


class MerchantInterface(ExchangeInterface):
    def __init__(self, name: str, content: List[Tuple[Items, Items]]) -> None:
        self.name = name
        self.content = content
        self.inventory = Container(name + "'s Wares")
    
    def exchange(self, source: Container, destination: Container, index: int, times: int | Literal["max"] = 1) -> None:
        if times == "max": times = min(min([source.content.get(i, 0) // self.content[index][0][i] for i in self.content[index][0]]), min([self.inventory.content.get(i, 0) // self.content[index][1][i] for i in self.content[index][1]]))

        if source.can_sub({i: self.content[index][0][i] * times for i in self.content[index][0]}) and self.inventory.can_sub({i: self.content[index][1][i] * times for i in self.content[index][1]}) and times > 0:
            source.sub({i: self.content[index][0][i] * times for i in self.content[index][0]})
            self.inventory.sub({i: self.content[index][1][i] * times for i in self.content[index][1]})
            destination.add({i: self.content[index][1][i] * times for i in self.content[index][1]})
        
        else: print("Insufficient ressources")



Bag = Container("Bag")
MoneyBag = Container("Money Bag")

Fruits = PoolGen(
{
    "Apple": (normal, (2, 5, 3, 3)),
    "Citrus": (normal, (2, 5, 3, 3)),
    "Banana": (normal, (2, 5, 3, 3)),
    "Orange": (normal, (2, 5, 3, 3)),
    "Rawsberry": (normal, (2, 5, 3, 3))
})
Bag.add(*Fruits.roll(10000))

FruitsBuyer = MerchantInterface("Fruits Buyer",
[
    ({"Apple": 5}, {"Gold": 4}),
    ({"Citrus": 5, "Banana": 3}, {"Gold": 5, "Copper": 5})
])
FruitsBuyer.inventory.add({"Gold": 10000, "Copper": 2000})

FruitsBuyer.exchange(Bag, MoneyBag, 0, "max")
FruitsBuyer.exchange(Bag, MoneyBag, 1, "max")


print(Bag, MoneyBag, sep="\n\n")