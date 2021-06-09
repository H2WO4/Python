# Import
from __future__ import annotations
from functools import reduce
from math import inf
from typing import Callable, Dict, List, Literal, Tuple
from random import choices, gauss


def normal(lowBound: float, highBound: float, mu: float, sigma: float) -> int:
    """ Normal distribution within bounds with automatic sigma """
    x = round(gauss(mu, (highBound - lowBound) / sigma))
    if lowBound <= x and x <= highBound:
        return x
    return normal(lowBound, highBound, mu, sigma)

def trim_dict(entry: Dict[str, int]) -> Dict[str, int]:
    """ Return the entry dictionary with 0-values removed """
    return {i: entry[i] for i in entry if entry[i] != 0}

def combine_dicts(*entry: Dict[str, int]) -> Dict[str, int]:
    """ Return the union of dictionaries where identical keys gets sumed up """
    return trim_dict(reduce(lambda d1, d2: {i: d1.get(i, 0) + d2.get(i, 0) for i in (d1 | d2)}, entry))

def mul_dict(entry: Dict[str, int], times: int) -> Dict[str, int]:
    """ Return the entry dictionaries with its values multiplied by times """
    return {i: entry[i] * times for i in entry}

def text_dict(entry: Dict[str, int]) -> str:
    """ Return a string representation of the dictionary to use in printing """
    return "\n".join(["{} x{}".format(i, entry[i]) for i in sorted(entry.keys())])


class Container:
    """ Object containg a dictionary and allowing new operations to be done  """
    def __init__(self) -> None:
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
        return text_dict(self.content)


class PoolGen:
    """ Object able to generate dictionaries based of random factors\n
    Structure of entries:\n
    {
        "Item1": (function1, (param1)),
        "Item2": (function2, (param2))
    } """
    def __init__(self, entries: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.content = entries
    
    def add(self, entries: Dict[str, Tuple[Callable[..., int], Tuple[float, ...]]]) -> None:
        self.content |= entries

    def roll(self, times: int = 1) -> List[Dict[str, int]]: 
        return [{i: self.content[i][0](*self.content[i][1])} for i in choices([j for j in self.content], k=times)]

    def __str__(self) -> str:
        return "\n".join("{}".format(x) for x in sorted(self.content))

def equiPool(items: List[str], method: Callable[..., int], distribution: Tuple[float, ...]) -> PoolGen:
    """ Generate a PoolGen with less data than usual\n
    Structure of variables:\n
    items = ["Item1", "Item2", ...]; method = function; distribution = param\n
    Giving a PoolGen with entries:\n
    {
        "Item1": (function, (param)),
        "Item2": (function, (param))
    } """
    return PoolGen({i: (method, distribution) for i in items})

def simiPool(items: Dict[str, Tuple[float, ...]], method: Callable[..., int]) -> PoolGen:
    """ Generate a PoolGen with less data than usual\n
    Structure of variables:\n
    items = {"Item1": param1, "Item2": param2, ...}; method = function\n
    Giving a PoolGen with entries:\n
    {
        "Item1": (function, (param1)),
        "Item2": (function, (param2))
    } """
    return PoolGen({i: (method, items[i]) for i in items})


class GenerationInterface:
    """ Object containing dictionaries pairs, allowing transforming a copy of the first one in the second\n
    Structure of content:\n
    [
        ({ItemGive1: amount1, ItemGive2, amount2}, {ItemReceive3: amount3}), # Exchange 1
        ({ItemGive4: amount4}, {ItemReceive5: amount5, ItemReceive6: amount6}), # Exchange 2
    ] """
    def __init__(self, name: str, content: List[Tuple[Dict[str, int], Dict[str, int]]]) -> None:
        self.name = name
        self.content = content
    
    def add(self, *content: Tuple[Dict[str, int], Dict[str, int]]) -> None:
        for i in content:
            self.content.append(i)

    def exchange(self, source: Container, destination: Container, index: int, times: int | Literal["max"] = 1) -> None:
        if times == "max": times = min([source.content[i] // self.content[index][0][i] for i in self.content[index][0]])
        if times <= 0: raise ValueError

        to_take = mul_dict(self.content[index][0], times)
        to_give = mul_dict(self.content[index][1], times)

        if source.can_sub(to_take):
            source.sub(to_take)
            destination.add(to_give)

    def __str__(self) -> str:
        return "{}:\n".format(self.name) + "\n".join(["[{}] {} -> {}".format(i+1, ", ".join(["{} x{}".format(j, self.content[i][0][j]) for j in self.content[i][0]]), ", ".join(["{} x{}".format(j, self.content[i][1][j]) for j in self.content[i][1]])) for i in range(len(self.content))])


class ExchangeInterface(GenerationInterface):
    """ Subclass of GenerationInterface\n
    Has in addition its Container, limiting its trade by its own ressources """
    def __init__(self, name: str, content: List[Tuple[Dict[str, int], Dict[str, int]]]) -> None:
        self.name = name
        self.content = content
        self.inventory = Inventory(self.name, Container())
    
    def exchange(self, source: Container, destination: Container, index: int, times: int | Literal["max"] = 1) -> None:
        if times == "max": times = min(min([source.content.get(i, 0) // self.content[index][0][i] for i in self.content[index][0]]), min([self.inventory.container.content.get(i, 0) // self.content[index][1][i] for i in self.content[index][1]]))
        if times <= 0: raise ValueError

        to_take = mul_dict(self.content[index][0], times)
        to_give = mul_dict(self.content[index][1], times)

        if source.can_sub(to_take) and self.inventory.container.can_sub(to_give):
            source.sub(to_take)
            self.inventory.container.sub(to_give)
            destination.add(to_give)


class CollectionPoint:
    """ Encapsulate a PoolGen into an higher-order object """
    members: Dict[str, CollectionPoint] = {}

    def __init__(self, name: str, pool: PoolGen) -> None:
        CollectionPoint.members[name] = self

        self.name = name
        self.pool = pool

    def __str__(self) -> str:
        return "{}:\n".format(self.name) + str(self.pool)


class Inventory:
    """ Encapsulate a Container into an higher-order object """
    members: Dict[str, Inventory] = {}

    def __init__(self, name: str, container: Container) -> None:
        Inventory.members[name] = self

        self.name = name
        self.container = container
    
    def __str__(self) -> str:
        return "{}:\n".format(self.name) + str(self.container)


Bag = Container()
MoneyBag = Container()

Fruits = equiPool(["Apple", "Citrus", "Banana", "Orange", "Rawsberry"], normal, (2, 5, 3, 3))

FruitsBuyer = ExchangeInterface("Fruits Buyer",
[
    ({"Apple": 5}, {"Gold": 4}),
    ({"Citrus": 5, "Banana": 3}, {"Gold": 5, "Copper": 5})
])
FruitsBuyer.inventory.container.add({"Gold": 10000, "Copper": 2000})


Self = Inventory("Self", Bag)
Orchard = CollectionPoint("Ochard", Fruits)

Self.container.add(*Orchard.pool.roll(100))

quitting = False
while not quitting:
    match input().split():
        case ["collect", x, n]:
            output = combine_dicts(*CollectionPoint.members[x].pool.roll(int(n)))
            print("You collected {} times in {} and found:\n{}\n".format(n, x, text_dict(output)))
            Bag.add(output)

        case ["see", x]:
            if x in Inventory.members:
                print(Inventory.members[x], "\n")

            elif x in CollectionPoint.members:
                print(CollectionPoint.members[x], "\n")

        case ["pause"]:
            pass

        case ["quit"]:
            quitting = True