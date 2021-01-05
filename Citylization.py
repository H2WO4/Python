import tkinter as tk
import os, json, glob



class City:
    def __init__(self, name, size):
        self.name = name
        self.size = size * 2 + 1
        self.grid = [[BuildingList["empty"] for j in range(size * 2 + 1)] for i in range(size * 2 + 1)]
        self.grid[size][size] = BuildingList["town_hall"]
    
    def endTurn(self):
        for i in self.grid:
            for j in i:
                j.activate()



class Ressource:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        self.amount = 0
        RessourceList[self.id] = self

    def __str__(self):
        return "{}: {}".format(self.name, self.amount)
    
    def gain(self, amount):
        self.amount += amount



class Building:
    def __init__(self, rawData):
        self.name = rawData["name"]
        self.id = rawData["id"]
        self.symbol = rawData["symbol"]
        self.description = rawData["description"]
        self.type = rawData["type"]
        self.yields = []
        for i in rawData["yields"]:
            self.yields.append(Yield(i, self))
        self.tags = []
        for i in rawData["tags"]:
            self.tags.append(Tag(i, self))
        
        BuildingList[self.id] = self
    
    def __str__(self):
        return self.symbol
    
    def hasTag(self, tag):
        for i in self.tags:
            if i.name == tag:
                return True
        return False
    
    def activate(self, x, y):
        for i in self.yields:
            i.produce(x, y)
    
    def neighbors(_, x, y):
        output = []
        for a, b in [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1] if (abs(a) + abs(b) > 0)]:
            try:
                output.append(City.grid[x+a][y+b])
            except:
                pass
        return output
    
    def neighbors_2(_, x, y):
        output = []
        for a, b in [(a, b) for a in [-2, -1, 0, 1, 2] for b in [-2, -1, 0, 1, 2] if (abs(a) + abs(b) > 0)]:
            try:
                output.append(City.grid[x+a][y+b])
            except:
                pass
        return output
    
    def direct_neighbors(_, x, y):
        output = []
        for a, b in [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1] if (abs(a) + abs(b) == 1)]:
            try:
                output.append(City.grid[x+a][y+b])
            except:
                pass
        return output
    
    def direct_neighbors_2(_, x, y):
        output = []
        for a, b in [(a, b) for a in [-2, -1, 0, 1, 2] for b in [-2, -1, 0, 1, 2] if (abs(a) + abs(b) in [1, 2])]:
            try:
                output.append(City.grid[x+a][y+b])
            except:
                pass
        return output



class Yield:
    def __init__(self, rawData, origin):
        self.type = rawData["type"]
        self.gains = []
        for i in rawData["gains"]:
            self.gains.append(Gain(i, self))
        self.origin = origin
    
    def produce(self, x, y):
        for i in self.gains:
            i.calculate(x, y)



class Gain:
    def __init__(self, rawData, origin):
        self.ressource = rawData["ressource"]
        self.amount = rawData["amount"]
        self.modifiers = []
        for i in rawData["modifiers"]:
            self.modifiers.append(Modifier(i, self))
        self.origin = origin
        
    def calculate(self, x, y):
        bonus = 0
        for i in self.modifiers:
            bonus += i.calculate(self.amount + bonus, x, y)
        RessourceList[self.ressource].gain(self.amount + bonus)



class Modifier:
    def __init__(self, rawData, origin):
        self.scope = rawData["scope"]
        self.type = rawData["type"]
        self.amount = rawData["amount"]
        self.targets = []
        for i in rawData["targets"]:
            self.targets.append(Target(i, self))
        self.origin = origin
        
    def calculate(self, amount, x, y):
        target = set({})
        bonus = 0
        for i in self.targets:
            target |= i.evaluate()

        if self.scope == "global":
            match = []
            [[match.append(j) for j in i if j in target] for i in City.grid]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "neighbors":
            match = []
            [match.append(i) for i in self.origin.origin.origin.neighbors(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "direct_neighbors":
            match = []
            [match.append(i) for i in self.origin.origin.origin.direct_neighbors(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "neighbors_2":
            match = []
            [match.append(i) for i in self.origin.origin.origin.neighbors_2(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "direct_neighbors_2":
            match = []
            [match.append(i) for i in self.origin.origin.origin.direct_neighbors_2(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        return bonus



class Target:
    def __init__(self, rawData, origin):
        self.type = rawData["type"]
        self.target = rawData["target"]
        self.origin = origin
    
    def evaluate(self):
        if self.type == "tag":
            return {BuildingList[i] for i in BuildingList if BuildingList[i].hasTag(self.target)}
        elif self.type == "building":
            return {BuildingList[self.target]}



class Tag:
    def __init__(self, rawData, origin):
        self.name = rawData["name"]
        self.origin = origin



class NewLabel(tk.Label):

    def __init__(self, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.bind("<Enter>", self.displayDescription)

    def displayDescription(self, _):
        descriptionText["text"] = City.grid[self.x][self.y].name + "\n" * 2 + City.grid[self.x][self.y].description + "\n" + " " * 100



BuildingListRaw = []
BuildingList = {}
BuildingImages = {}

RessourceList = {}



path = "/Citylization"
for filename in glob.glob(os.path.join(os.getcwd() + path, "*.json")):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        BuildingListRaw.append(json.load(f))

for data in BuildingListRaw:
    Building(data)

citySize = 9

City = City("A", citySize//2)

Gold = Ressource("Gold", "gold")
Wheat = Ressource("Wheat", "wheat")
Fish = Ressource("Fish", "fish")
Wood = Ressource("Wood", "wood")


""" Graphical Interface """


# Define the update function
def update():
    for i in range(citySize):
        for j in range(citySize):
            try:
                gridText[i][j]["image"] = BuildingImages[City.grid[i][j].id]
            except:
                gridText[i][j]["text"] = City.grid[i][j].symbol
    
    ressourceText["text"] = "\n".join(["{}: {}".format(RessourceList[i].name, RessourceList[i].amount) for i in RessourceList]) + ("\n" + " " * 40)


# Define the end turn command
def endTurn():
    for i in range(City.size):
        for j in range(City.size):
            City.grid[i][j].activate(i, j)
    
    update()


# Define the build command
def build(building, x, y):
    if City.grid[x][y].hasTag("empty"):
        City.grid[x][y] = building
        update()


# Define the main window
main = tk.Tk()
main.title("Citylization")


# Load images
path = "/CitylizationImages"
for filename in glob.glob(os.path.join(os.getcwd() + path, "*.png")):
    BuildingImages[filename.removeprefix(os.getcwd() + path + "\\").removesuffix(".png")] = tk.PhotoImage(file=filename)



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
        grid[i].append(tk.Frame(borderwidth=3, relief="groove", background="white"))
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

descriptionText = tk.Label(master=descriptionPanel, text=" " * 100, background="white")
descriptionText.pack()


# Define the end turn button
endTurnGroup = tk.Frame()
endTurnGroup.grid(row=citySize+1, column=citySize+1)

endTurnButton = tk.Button(text="End Turn", master=endTurnGroup, command=endTurn)
endTurnButton.pack()


# Define the menu buttons
menuGroup = tk.Frame()
menuGroup.grid(row=citySize+1, column=citySize+2)

buildButton = tk.Button(text="Build", master=menuGroup, command=endTurn)
buildButton.pack()


# Setup windows resizing
[main.columnconfigure(i, weight=1) for i in range(citySize)]
main.columnconfigure(citySize+1, weight=4)
[main.rowconfigure(i, weight=1) for i in range(citySize)]
main.rowconfigure(citySize+1, weight=4)


# Tests
def test():
    build(BuildingList["farm"], 3, 2)
    build(BuildingList["farm"], 4, 2)

    build(BuildingList["small_house"], 2, 6)
    build(BuildingList["small_house"], 2, 5)
    build(BuildingList["small_house"], 1, 6)

    build(BuildingList["bar"], 3, 6)

    build(BuildingList["woods"], 0, 0)
    build(BuildingList["woods"], 0, 1)
    build(BuildingList["woods"], 1, 0)

    build(BuildingList["woodcutter"], 1, 1)

    build(BuildingList["fisher"], 6, 6)

    for i in range(citySize):
        build(BuildingList["river"], 5, i)

# Start the window
update()
test()
main.mainloop()