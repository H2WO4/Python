from random import choice
from typing import List


class Treasure:
    def __init__(self, name: str, iType: str, rarity: str, price: int):
        self.name = name
        self.type = iType
        self.rarity = rarity
        self.price = price
        self.quantity = 0

    def __str__(self):
        return "{}: {}".format(self.name, self.quantity)

class Chest:
    def __init__(self, content: List[Treasure]):
        self.content = content
    
    def __str__(self):
        output: List[str] = []
        for i in self.content:
            output.append(i.name)
        return str(output)
    

class Pool:
    def __init__(self, name: str, objects: List[Treasure]):
        self.name = name
        self.objects = objects

    def roll(self, rolls: int):
        output: List[Treasure] = []
        for i in range(rolls):
            output.append(choice(self.objects))
        for i in output:
            i.quantity += 1
        
        return Chest(output)
            

class SalvagingPoint: 
    def __init__(self, name: str, pools: List[Pool]):
        self.name = name
        self.pools = pools

class Cylinders:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

totalMoney = 0

Bolt = Treasure("Bolt", "Mechanical", "Common", 20)
Gear = Treasure("Gear", "Mechanical", "Common", 30)
Rod = Treasure("Rod", "Mechanical", "Common", 50)

BasicPool = Pool("Basic Pool", [Bolt, Gear, Rod])

print(BasicPool.roll(5))
