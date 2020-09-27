from random import choice

class Treasure:
    def __init__(self, name, iType, rarity, price):
        self.name = name
        self.type = iType
        self.rarity = rarity
        self.price = price
        self.quantity = 0

    def __str__(self):
        return "{}: {}".format(self.name, self.quantity)

class Chest:
    def __init__(self, content):
        self.content = content
    
    def __str__(self):
        output = []
        for i in self.content:
            output.append(i.name)
        return str(output)
    

class Pool:
    def __init__(self, name, objects):
        self.name = name
        self.objects = objects

    def roll(self, rolls):
        output = []
        for i in range(rolls):
            output.append(choice(self.objects))
        for i in output:
            i.quantity += 1
        return Chest(output)
            

class SalvagingPoint: 
    def __init(self, name, pools):
        self.name = name
        self.pools = pools

class Cylinders:
    def __init__(self, name, level):
        self.name = name
        self.level = level

totalMoney = 0

Bolt = Treasure("Bolt", "Mechanical", "Common", 20)
Gear = Treasure("Gear", "Mechanical", "Common", 30)
Rod = Treasure("Rod", "Mechanical", "Common", 50)

BasicPool = Pool("Basic Pool", [Bolt, Gear, Rod])

print(BasicPool.roll(5))
