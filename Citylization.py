import os, json, glob


class City:
    def __init__(self, name, size):
        self.name = name
        self.grid = [[getBuildingById("empty") for j in range(size * 2 + 1)] for i in range(size * 2 + 1)]
        self.grid[size][size] = getBuildingById("town_hall")
        self.grid[1][1] = getBuildingById("farm")
        self.grid[2][1] = getBuildingById("farm")
        self.grid[1][2] = getBuildingById("small_house")
        self.grid[3][2] = getBuildingById("small_house")
        self.grid[1][3] = getBuildingById("small_house")
    
    def endTurn(self):
        for i in self.grid:
            for j in i:
                j.activate()



class Ressource:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        self.amount = 0
        RessourceList.append(self)

    def __str__(self):
        return "{}: {}".format(self.name, self.amount)
    
    def gain(self, amount):
        self.amount += amount



class Building:
    def __init__(self, rawData):
        self.name = rawData["name"]
        self.id = rawData["id"]
        if len(rawData["symbol"]) > 3:
            self.symbol = chr(int(rawData["symbol"]))
        else:
            self.symbol = rawData["symbol"]
        self.type = rawData["type"]
        self.yields = []
        for i in rawData["yields"]:
            self.yields.append(Yield(i, self))
        self.tags = []
        for i in rawData["tags"]:
            self.tags.append(Tag(i, self))
    
    def __str__(self):
        return self.symbol
    
    def hasTag(self, tag):
        for i in self.tags:
            if i.name == tag:
                return True
        return False
    
    def activate(self):
        for i in self.yields:
            i.produce()



class Yield:
    def __init__(self, rawData, origin):
        self.type = rawData["type"]
        self.gains = []
        for i in rawData["gains"]:
            self.gains.append(Gain(i, self))
        self.origin = origin
    
    def produce(self):
        for i in self.gains:
            i.calculate()



class Gain:
    def __init__(self, rawData, origin):
        self.ressource = rawData["ressource"]
        self.amount = rawData["amount"]
        self.modifiers = []
        for i in rawData["modifiers"]:
            self.modifiers.append(Modifier(i, self))
        self.origin = origin
        
    def calculate(self):
        bonus = 0
        for i in self.modifiers:
            bonus += i.calculate()
        getRessourceById(self.ressource).gain(self.amount + bonus)



class Modifier:
    def __init__(self, rawData, origin):
        self.scope = rawData["scope"]
        self.type = rawData["type"]
        self.amount = rawData["amount"]
        self.targets = []
        for i in rawData["targets"]:
            self.targets.append(Target(i, self))
        self.origin = origin
        
    def calculate(self):
        target = set({})
        bonus = 0
        for i in self.targets:
            target = target | i.evaluate()
        if self.scope == "global":
            match = []
            [[match.append(1) for j in i if j in target] for i in City.grid]
            bonus += len(match)
        return bonus



class Target:
    def __init__(self, rawData, origin):
        self.type = rawData["type"]
        self.target = rawData["target"]
        self.origin = origin
    
    def evaluate(self):
        if self.type == "tag":
            return {i for i in BuildingList if i.hasTag(self.target)}
        elif self.type == "building":
            return {getBuildingById(self.target)}



class Tag:
    def __init__(self, rawData, origin):
        self.name = rawData["name"]
        self.origin = origin



BuildingListRaw = []
BuildingList = []

RessourceList = []



def getBuildingByName(name):
    for i in BuildingList:
        if i.name == name:
            return i

def getBuildingById(Id):
    for i in BuildingList:
        if i.id == Id:
            return i

def getRessourceByName(name):
    for i in RessourceList:
        if i.name == name:
            return i

def getRessourceById(Id):
    for i in RessourceList:
        if i.id == Id:
            return i



path = "/Citylization"
for filename in glob.glob(os.path.join(os.getcwd() + path, "*.json")):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        BuildingListRaw.append(json.load(f))

for data in BuildingListRaw:
    BuildingList.append(Building(data))



City = City("A", 2)

Gold = Ressource("Gold", "gold")
Wheat = Ressource("Wheat", "wheat")
Fish = Ressource("Fish", "fish")
Wood = Ressource("Wood", "wood")

for i in City.grid:
    print(" ".join([str(j) for j in i]))

for i in City.grid:
    for j in i:
        j.activate()

for i in RessourceList:
    print(i)