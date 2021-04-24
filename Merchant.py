from typing import Any, Callable, Dict, List, Tuple
from random import choices, gauss, uniform


class Item:

    def __init__(self, name: str, amount: int = 1) -> None:
        self.name = name
        self.amount = amount
    
    def __eq__(self, other):
        if not isinstance(other, Item):
            return TypeError

        return self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Item):
            return TypeError

        return self.name < other.name

    def __str__(self) -> str:
        return "{} ×{}".format(self.name, self.amount)


class Inventory:

    def __init__(self, name: str) -> None:
        self.name = name
        self.content: List[Item] = []
    
    def add(self, other) -> None:
        if not isinstance(other, Item):
            raise TypeError

        for i in self.content:
            if i == other:
                i.amount += other.amount
                break
        else:
            self.content.append(other)
    
    def __str__(self) -> str:
        return "{}:\n".format(self.name) + "\n".join([str(i) for i in self.content])


class PoolGen:

    def __init__(self, content: Dict[str, Tuple[int, ...]], method: Callable[..., float]) -> None:
        self.content = content
        self.method = method
    
    def roll(self, times: int = 1) -> List[Item]:
        return [Item(i, round(self.method(*self.content[i]))) for i in choices([j for j in self.content], k=times)]


def equiPool(items: List[str], distribution: Tuple[int, ...], method: Callable[..., float]) -> PoolGen:
    content = {}
    for i in items:
        content[i] = distribution
    return PoolGen(content, method)





A = Inventory("Bag")

Fruits = equiPool(["Apple", "Orange", "Banana", "Pineapple"], (2, 5), uniform)
for i in Fruits.roll(100):
    A.add(i)

print(A)