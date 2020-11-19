from math import floor
from random import choice, random, randint



class UnremovableBuilding(Exception):
    def __init__(self):
        self.message = "Trying to remove a building that cannot be destroyed"
    
    def __str__(self):
        return self.message

class OccupiedSpace(Exception):
    def __init__(self):
        self.message = "Trying to build in a place that is already occupied"

    def __str__(self):
        return self.message

class OutOfGrid(Exception):
    def __init__(self):
        self.message = "Trying to interact with a space outside of the grid"

    def __str__(self):
        return self.message



class Building:
    def __init__(self, name, icon, description = "Lorem Ipsum"):
        self.name = name
        self.icon = icon
        self.description = description

    def __str__(self):
        return self.name + ":\n" + self.description + "\n"


class Ressource:
    def __init__(self, name):
        self.name = name
        self.quantity = 0
        return None

    def gain(self, quantity):
        if quantity >= 0:
            self.quantity += floor(quantity)
        return None
    
    def lose(self, quantity):
        if quantity >= 0:
            self.quantity -= floor(quantity)
        return None
    
    def change(self, quantity):
        self.quantity += floor(quantity)
        return None

    def __str__(self):
        return self.name + ": " + str(self.quantity) + "\n"


class City:
    def __init__(self, name, size, terrain = True):
        self.name = name
        self.size = size * 2 + 1
        self.grid = []
        for i in range(self.size):
            self.grid.append([])
            for _ in range(self.size):
                self.grid[i].append(Empty)
        self.build(size, size, Center)
        if terrain and size > 1:
            self.additionalTerrain()
        return None
    
    def additionalTerrain(self):
        river = [*range(1, self.size - 1)]
        river.pop(floor(self.size / 2 - 1))
        river = choice(river)
        if floor(random() * 2):
            for i in range(self.size):
                self.build(i, river, River)
        else:
            for i in range(self.size):
                self.build(river, i, River)
        
        for i in range(self.size):
            woods = [randint(0, self.size - 1), randint(0, self.size - 1)]
            while self.look(woods[0], woods[1]) != Empty:
                woods = [randint(0, self.size - 1), randint(0, self.size - 1)]
            self.build(woods[0], woods[1], Woods)
        return None
    
    def __str__(self):
        grid = ""
        for i in range(self.size):
            for j in range(self.size):
                grid += self.grid[i][j].icon
                if j < self.size - 1:
                    grid += " "
            grid += "\n"
        return grid
    
    def look(self, x, y):
        if (x in [*range(0, self.size - 1)]) and (y in [*range(0, self.size - 1)]):
            return self.grid[x][y]
        raise OutOfGrid()
    
    def build(self, x, y, building):
        if (x in [*range(0, self.size - 1)]) and (y in [*range(0, self.size - 1)]):
            if self.look(x,y) == Empty:
                self.grid[x][y] = building
                return None
            raise OccupiedSpace()
        raise OutOfGrid()
    
    def destroy(self, x, y):
        if (x in [*range(0, self.size - 1)]) and (y in [*range(0, self.size - 1)]):
            if not self.look(x, y) in [Center, River, Empty]:
                self.grid[x][y] = Empty
                return None
            raise UnremovableBuilding()
        raise OutOfGrid()
    
    def checkNeighbourgs(self, x, y):
        neighbourgs = []
        if y + 1 < self.size:
            neighbourgs.append(self.grid[x][y+1])
        if x + 1 < self.size:
            neighbourgs.append(self.grid[x+1][y])
        if y - 1 >= 0:
            neighbourgs.append(self.grid[x][y-1])
        if x - 1 >= 0:
            neighbourgs.append(self.grid[x-1][y])
        return neighbourgs

    def turnEnd(self):
        x, y = 0, 0
        for i in self.grid:
            for j in i:
                if j == Center:
                    Gold.gain(5)
                
                if j == Farm:
                    gain = 2
                    neighbourgs = self.checkNeighbourgs(x, y)
                    if River in neighbourgs:
                        gain += 2
                    for k in neighbourgs:
                        if k is Farm:
                            gain += 0.5
                    Wheat.gain(gain)
                
                if j == Woods:
                    gain = 0
                    neighbourgs = self.checkNeighbourgs(x, y)
                    for k in neighbourgs:
                        if k is Woods:
                            gain += 1
                        if k is Woodcutter:
                            gain -= 1
                    Wood.gain(gain)
                
                if j == Woodcutter:
                    gain = 0
                    neighbourgs = self.checkNeighbourgs(x, y)
                    for k in neighbourgs:
                        if k is Woods:
                            gain += 2
                    Wood.gain(gain)
                
                x += 1
            x = 0
            y += 1
        print(City)
        ressourceCheck()
        return None


def ressourceCheck():
    print(Wheat)
    print(Wood)
    print(Gold)
    return None



Empty = Building("Empty Land", "-", "Free terrain suitable for construction.")
River = Building("River", "≈", "A flowing body of water, provide water to adjacent tiles.")
Woods = Building("Woods", "W", "A small patch of tree, boosting both the attractiveness of nearby tiles and helping providing ressources")

Center = Building("City Center", "*", "The center of the town, providing bonus to most neighbouring buildings.")
Farm = Building("Farm", "F", "A simple farm. Produce more if provided with water.")
Woodcutter = Building("Woodcutter's Cabin", "C", "A small hut for a woodcutter. Produces wood only if adjacent to Woods tile.")

Wheat = Ressource("Wheat")
Wood = Ressource("Wood")
Gold = Ressource("Gold")



name = input("Name of the city ? ")
size = input("Radius of the city ? ")
nature = input("Do you want additional terrain generation ? (Y/N) ").lower()
if nature == "y":
    nature = True
else:
    nature = False

City = City(name, int(size), nature)

print(City)
ressourceCheck()



quit = False

while not quit:
    command = input("What do you want to do ? ").lower()

    if command == "look":
        command = eval(input("Which tile ? [x, y] "))
        print(City.look(int(command[0]) - 1, int(command[1]) - 1))
    
    if command == "check":
        print(City)
        ressourceCheck()
    
    if command == "build":
        building = input("What do you want to build ? ")
        command = eval(input("Where do you want to build it ? [x, y] "))
        City.build(int(command[0]) - 1, int(command[1]) - 1, building)
        City.turnEnd()

    if command == "destroy":
        command = eval(input("Where do you want to destroy a building ? [x, y] "))
        City.destroy(int(command[0]) - 1, int(command[1]) - 1)
        City.turnEnd()

    if command == "wait":
        City.turnEnd()
    
    if command == "quit":
        quit = True