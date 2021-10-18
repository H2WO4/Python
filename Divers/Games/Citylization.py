from __future__ import annotations
import tkinter as tk
import os, json, glob
from typing import Any, Dict, List, Set, Tuple


def neighbors(x: int, y: int) -> Tuple[Building, ...]:
    output: List[Building] = []
    for a, b in [(a, b) for a in range(-1, 2) for b in range(-1, 2) if (abs(a) + abs(b) > 0)]:
        try:
            output.append(newCity[x+a, y+b])
        except:
            pass
    return tuple(output)
def neighbors_2(x: int, y: int) -> Tuple[Building, ...]:
    output: List[Building] = []
    for a, b in [(a, b) for a in range(-2, 3) for b in range(-2, 3) if (abs(a) + abs(b) > 0)]:
        try:
            output.append(newCity[x+a, y+b])
        except:
            pass
    return tuple(output)
def direct_neighbors(x: int, y: int) -> Tuple[Building, ...]:
    output: List[Building] = []
    for a, b in [(a, b) for a in range(-1, 2) for b in range(-1, 2) if (abs(a) + abs(b) == 1)]:
        try:
            output.append(newCity[x+a, y+b])
        except:
            pass
    return tuple(output)
def direct_neighbors_2(x: int, y: int) -> Tuple[Building, ...]:
    output: List[Building] = []
    for a, b in [(a, b) for a in range(-2, 3) for b in range(-2, 3) if (abs(a) + abs(b) in {1, 2})]:
        try:
            output.append(newCity[x+a, y+b])
        except:
            pass
    return tuple(output)

class Ressource:
    def __init__(self, name: str, Id: str) -> None:
        self.name = name
        self.id = Id
        self.amount = 0
        RessourceList[self.id] = self

    def __str__(self) -> str:
        return "{}: {}".format(self.name, self.amount)
    
    def gain(self, amount: int) -> None:
        self.amount += amount

class Building:
    def __init__(self, rawData: Dict[str, Any]) -> None:
        self.name: str = rawData["name"]
        self.id: str = rawData["id"]
        self.symbol: str = rawData["symbol"]
        self.description: str = rawData["description"]
        self.type: str = rawData["type"]
        self.yields: List[Yield] = []
        for i in rawData["yields"]: self.yields.append(Yield(i))
        self.tags: List[Tag] = []
        for i in rawData["tags"]: self.tags.append(Tag(i))
        
        BuildingList[self.id] = self
    
    def __str__(self) -> str: return self.symbol
    
    def hasTag(self, tag: str) -> bool:
        for i in self.tags:
            if i.name == tag: return True
        return False
    
    def activate(self, x: int, y: int) -> None:
        for i in self.yields: i.produce(x, y)

class Yield:
    def __init__(self, rawData: Dict[str, Any]) -> None:
        self.type: str = rawData["type"]
        self.gains: List[Gain] = []
        for i in rawData["gains"]: self.gains.append(Gain(i))
    
    def produce(self, x: int, y: int) -> None:
        for i in self.gains: i.calculate(x, y)

class Gain:
    def __init__(self, rawData: Dict[str, Any]) -> None:
        self.ressource: str = rawData["ressource"]
        self.amount: int = rawData["amount"]
        self.modifiers: List[Modifier] = []
        for i in rawData["modifiers"]: self.modifiers.append(Modifier(i))
        
    def calculate(self, x: int, y: int) -> None:
        bonus = 0
        for i in self.modifiers: bonus += i.calculate(self.amount + bonus, x, y)
        RessourceList[self.ressource].gain(self.amount + bonus)

class Modifier:
    def __init__(self, rawData: Dict[str, Any]) -> None:
        self.scope: str = rawData["scope"]
        self.type: str = rawData["type"]
        self.amount: int = rawData["amount"]
        self.targets: List[Target] = []
        for i in rawData["targets"]: self.targets.append(Target(i))
        
    def calculate(self, amount: int, x: int, y: int) -> int:
        target: Set[Building] = set({})
        bonus = 0
        for i in self.targets: target |= i.evaluate()

        match: List[Building] = []
        if self.scope == "global":
            [[match.append(j) for j in i if j in target] for i in newCity.grid]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "neighbors":
            [match.append(i) for i in neighbors(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "direct_neighbors":
            [match.append(i) for i in direct_neighbors(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "neighbors_2":
            [match.append(i) for i in neighbors_2(x, y) if i in target]
            if self.type == "additive":
                bonus += len(match) * self.amount
            if self.type == "multiplicative":
                bonus += amount * ((len(match) - 1) * self.amount)
            if self.type == "boolean_additive" and len(match) >= 1:
                bonus += self.amount
            if self.type == "boolean_multiplicative" and len(match) >= 1:
                bonus += amount * (self.amount - 1)
        
        elif self.scope == "direct_neighbors_2":
            [match.append(i) for i in direct_neighbors_2(x, y) if i in target]
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
    def __init__(self, rawData: Dict[str, Any]) -> None:
        self.type: str = rawData["type"]
        self.target: str = rawData["target"]
    
    def evaluate(self) -> set[Building]:
        if self.type == "tag":
            return {BuildingList[i] for i in BuildingList if BuildingList[i].hasTag(self.target)}
        return {BuildingList[self.target]}

class Tag:
    def __init__(self, rawData: Dict[str, Any]) -> None:
        self.name: str = rawData["name"]

class City:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size * 2 + 1
        self.grid: List[List[Building]] = [[BuildingList["empty"] for _ in range(size * 2 + 1)] for _ in range(size * 2 + 1)]
        self.grid[size][size] = BuildingList["town_hall"]
    
    def __getitem__(self, key: Tuple[int, int]) -> Building: return self.grid[key[0]][key[1]]
    
    def __setitem__(self, key: Tuple[int, int], other: Building) -> None: self.grid[key[0]][key[1]] = other
    
    def endTurn(self) -> None:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self[i,j].activate(i, j)

class GridLabel(tk.Label):

    def __init__(self, x: int, y: int, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.bind("<Enter>", self.displayDescription)

    def displayDescription(self, _: Any) -> None: descriptionText["text"] = newCity[self.x, self.y].name + "\n" * 2 + newCity[self.x, self.y].description + "\n" + " " * 100

BuildingListRaw: List[Dict[str, Any]] = []
BuildingList: Dict[str, Building] = {}
BuildingImages: Dict[str, tk.Image] = {}

RessourceList: Dict[str, Ressource] = {}

path = "/Divers/Citylization"
for filename in glob.glob(os.path.join(os.getcwd() + path, "*.json")):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        BuildingListRaw.append(json.load(f))
for data in BuildingListRaw:
    Building(data)

citySize = 9

newCity = City("A", citySize//2)
turn = 0

Gold = Ressource("Gold", "gold")
Wheat = Ressource("Wheat", "wheat")
Fish = Ressource("Fish", "fish")
Wood = Ressource("Wood", "wood")


""" Graphical Interface """

# Define the update function
def update() -> None:
    for i in range(citySize):
        for j in range(citySize):
            try:
                gridText[i][j]["image"] = BuildingImages[newCity[i,j].id]
            except:
                gridText[i][j]["text"] = newCity[i,j].symbol
    
    ressourceText["text"] = "\n".join(["{}: {}".format(RessourceList[i].name, RessourceList[i].amount) for i in RessourceList]) + ("\n" + " " * 40)

# Define the end turn command
def endTurn() -> None:
    global turn
    turn += 1
    logText.append("Turn {} ended".format(turn))
    consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])
    
    for i in range(newCity.size):
        for j in range(newCity.size):
            newCity[i,j].activate(i, j)
    
    update()

# Define the build command
def build(building: Building, x: int, y: int) -> None:
    if newCity[x, y].hasTag("empty"):
        newCity[x, y] = building
        update()


# Define the main window
main = tk.Tk()
main.title("Citylization")


# Load images
path = "/Divers/CitylizationImages"
for filename in glob.glob(os.path.join(os.getcwd() + path, "*.png")):
    BuildingImages[filename.removeprefix(os.getcwd() + path + "\\").removesuffix(".png")] = tk.PhotoImage(file=filename)



# Define the console outputting text
console = tk.Frame(borderwidth=3, relief="sunken", background="white")
console.grid(row=citySize+1, column=0, columnspan=citySize, sticky="news")

logText = ["Welcome to Citylization!", "", "", ""]
consoleText = tk.Label(master=console, text="\n".join(logText[-4:-1] + [logText[-1]]), background="white")
consoleText.pack()


# Define the main grid
grid: List[List[tk.Frame]] = []
gridText: List[List[GridLabel]] = []
for i in range(citySize):
    grid.append([])
    gridText.append([])
    for j in range(citySize):
        grid[i].append(tk.Frame(borderwidth=3, relief="groove", background="white"))
        grid[i][j].grid(row=i, column=j, sticky="news")
        gridText[i].append(GridLabel(i, j, master=grid[i][j], text="", background="white"))
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
[main.columnconfigure(i, weight=1) for i in range(citySize)] # type: ignore
main.columnconfigure(citySize+1, weight=4) # type: ignore
[main.rowconfigure(i, weight=1) for i in range(citySize)] # type: ignore
main.rowconfigure(citySize+1, weight=4) # type: ignore


# Tests
def test() -> None:
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
    
    update()

# Start the window
update()
test()
main.mainloop()