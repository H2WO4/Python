import tkinter as tk
import os, json, glob


class City:
    def __init__(self, name, size):
        self.name = name
        self.grid = [[getBuildingById("empty") for j in range(size * 2 + 1)] for i in range(size * 2 + 1)]
        self.grid[size][size] = getBuildingById("town_hall")
    
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
        if self.scope == "":
            pass
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



class NewLabel(tk.Label):

    def __init__(self, x, y, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.x = x
        self.y = y
        self.bind("<Enter>", self.displayDescription)

    def displayDescription(self, _):
        descriptionText["text"] = City.grid[self.x][self.y].name + "\n" + " " * 40



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

citySize = 7

City = City("A", citySize//2)

Gold = Ressource("Gold", "gold")
Wheat = Ressource("Wheat", "wheat")
Fish = Ressource("Fish", "fish")
Wood = Ressource("Wood", "wood")


""" Graphical Interface """


def update():
    for i in range(citySize):
        for j in range(citySize):
            gridText[i][j]["text"] = City.grid[i][j].symbol
    
    ressourceText["text"] = "\n".join(["{}: {}".format(i.name, i.amount) for i in RessourceList]) + ("\n" + " " * 40)


def endTurn():
    for i in City.grid:
        for j in i:
            j.activate()
    
    update()


# Define the main window
main = tk.Tk()
main.title("Citylization")


# Define the console outputting text
console = tk.Frame(borderwidth=3, relief="sunken", background="white")
console.grid(row=citySize+1, column=0, columnspan=citySize, sticky="news")

logText = ["Welcome to Citylization!", " " * 80, "", ""]
consoleText = tk.Label(master=console, text="\n".join(logText[-4:-1] + [logText[-1]]), background="white")
consoleText.pack()


# Define the main grid
grid = []
gridText = []
for i in range(citySize):
    grid.append([])
    gridText.append([])
    for j in range(citySize):
        grid[i].append(tk.Frame(borderwidth=3, relief="sunken", background="white"))
        grid[i][j].grid(row=i, column=j, sticky="news")
        gridText[i].append(NewLabel(i, j, master=grid[i][j], text="", background="white"))
        gridText[i][j].pack()


# Define the ressource list
ressourcesPanel = tk.Frame(borderwidth=3, relief="sunken", background="white")
ressourcesPanel.grid(row=0, column=citySize+1, rowspan=citySize, sticky="news")

ressourceText = tk.Label(master=ressourcesPanel, text="", background="white")
ressourceText.pack()


# Define the description panel
descriptionPanel = tk.Frame(borderwidth=3, relief="sunken", background="white")
descriptionPanel.grid(row=0, column=citySize+2, rowspan=citySize, sticky="news")

descriptionText = tk.Label(master=descriptionPanel, text=" " * 40, background="white")
descriptionText.pack()


# Define the end turn button
endTurnGroup = tk.Frame()
endTurnGroup.grid(row=citySize+1, column=citySize+1)

endTurnButton = tk.Button(text="End Turn", master=endTurnGroup, command=endTurn)
endTurnButton.pack()


# Setup windows resizing
[main.columnconfigure(i, weight=1) for i in range(citySize)]
main.columnconfigure(citySize+1, weight=4)
[main.rowconfigure(i, weight=1) for i in range(citySize)]
main.rowconfigure(citySize+1, weight=4)


# Tests
City.grid[2][2] = getBuildingById("farm")
City.grid[3][2] = getBuildingById("farm")

City.grid[2][5] = getBuildingById("small_house")
City.grid[3][5] = getBuildingById("small_house")
City.grid[2][6] = getBuildingById("small_house")

City.grid[3][6] = getBuildingById("bar")

City.grid[0][0] = getBuildingById("woods")
City.grid[0][1] = getBuildingById("woods")
City.grid[1][0] = getBuildingById("woods")

City.grid[1][1] = getBuildingById("woodcutter")

City.grid[5][4] = getBuildingById("fisher")

for i in range(citySize):
    City.grid[4][i] = getBuildingById("river")

# Start the window
update()
main.mainloop()