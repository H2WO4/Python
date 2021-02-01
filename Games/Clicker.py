""" Module Import """
from time import sleep
from threading import Thread
from typing import Any, Callable, Dict, List, Tuple, Union

""" Object Definition """
class Currency:
    def __init__(self, name: str, value: int = 0):
        self.name = name
        self.value = value

        currencies[self.name] = self

    def __str__(self) -> str:
        return "{} : {}".format(self.name, int(self.value))


class Building:
    def __init__(self, name: str, description: str, priceFormula: Tuple[Callable[[int], float], str], count: int = 0, **formula: Tuple[Union[Callable, str], ...]):
        self.name = name
        self.description = description
        self.formula: Dict[str, Tuple[Union[Callable, str], ...]] = formula
        self.priceFormula = priceFormula
        self.price = int(priceFormula[0](count))
        self.count = count
        
        buildings[self.name] = self

    def __str__(self) -> str:
        return "{} : {}\tCost: {}".format(self.name, self.count, self.price)
    
    def strPrice(self, n: int) -> str:
        return "{} : {}\tCost ({}): {}".format(self.name, self.count, n, self.bulkPrice(n))

    def produce(self) -> List[Tuple[Any, str]]:
        return [(eval("self.formula[i][0]({})".format(",".join([str(self.formula[i][j]) for j in range(1, len(self.formula[i]))]))), i) for i in self.formula]

    def buy(self, n: int) -> bool:
        requiredPrice = self.bulkPrice(n)
        if eval("{}.value >= {}".format(self.priceFormula[1], requiredPrice)):
            self.count += n
            
            exec("{}.value -= {}".format(self.priceFormula[1], self.price))
            self.price = int(self.priceFormula[0](self.count))
            return True
        
        return False

    def bulkPrice(self, n: int) -> int:
        price = 0
        for i in range(n):
            price += int(self.priceFormula[0](self.count+i))
        
        return price


""" Function Definition """
def passiveLoop() -> None:
    while True:
        for i in buildings:
            for j in buildings[i].produce():
                exec("{}.value += {}/5".format(j[1], j[0]))
        
        sleep(0.2)

def displayCurrencies() -> None:
    for i in currencies:
        print(currencies[i])

def displayBuildings() -> None:
    for i in buildings:
        print(buildings[i])

def displayBuildingsCost(n: int) -> None:
    for i in buildings:
        print(buildings[i].strPrice(n))

""" List Setup """
currencies: Dict[str, Currency] = {}
buildings: Dict[str, Building] = {}

""" Object Creation """
Cookies = Currency("Cookies")

Grandma = Building("Grandma", "A nice grandma that will bake some cookies.", (lambda n: 10 * (1.3 ** n), "Cookies"), 3, Cookies = (lambda n, m: n * (1 + m/2), "self.count", "Grandpa.count"))
Grandpa = Building("Grandpa", "This nice grandpa will help grandma to bake cookies", (lambda n: 50 * (1.4 ** n), "Cookies"), 0)
Factory = Building("Factory", "Now you're thinking with mass-production!", (lambda n: 250 * (1.3 ** n), "Cookies"), 0, Cookies = (lambda n: (n ** 2 + n) / 2, "self.count"))

""" Main Game Loop """
Thread(target = passiveLoop, daemon=True).start()
leave = False
while not leave:
    displayCurrencies()
    command = input().lower()

    if command in {"buy", "build"}:
        displayBuildings()
        command = input().title()
        if command in buildings:
            exec("{}.buy(1)".format(command))

    if command in {"buybulk", "buildbulk", "buy bulk", "build bulk"}:
        n = int(input("How much : "))
        displayBuildingsCost(n)
        command = input().title()
        if command in buildings:
            exec("{}.buy({})".format(command, n))

    if command in {"check", "status"}:
        displayCurrencies()
        displayBuildings()

    if command in {"quit", "leave"}:
        leave = True

    if command in {"cheat"}:
        Cookies.value *= 30