""" Importing Ressources """

import tkinter as tk
from typing import Any, Tuple



""" Object Definition """

class Group:
    """
    The Group object is used to represent a list of elements\n
    It contains information about its name, as well as an ordered list of its members
    """

    def __init__(self, name: str) -> None:
        """ Initialize a Group object """
        # Init - Setting attributes
        self.name = name
        self.elements = []

        # Init - Adding itself to lists for future indexing
        Groups[self.name] = self


    def __str__(self) -> str:
        """ Return the name value of the object """
        # Overload the 'str()' operator to return the group's name
        return self.name
    
    def isOnlyNonReveal(self) -> bool:
        for i in self.elements:
            if i.revealed:
                return True
        return False



class Element:
    """
    The Element object is used to represent a singular element\n
    It contains information about its name, in which group it belongs,
    its state and the list of its recipes
    """

    def __init__(self, name: str, recipes: str, group: Group = None, revealed: bool = False) -> None:
        """ Initialize an Element object """
        # Init - Setting attributes
        self.name = name
        self.recipes = recipes
        self.group = group
        self.revealed = revealed

        # Init - Adding itself to lists for future indexing
        Elements[self.name] = self
        if group is not None:
            group.elements.append(self)

        if revealed:
            ElementsCreated[self.name] = self
        else:
            ElementsNotCreated[self.name] = self


    def __str__(self) -> str:
        """ Return the name value of the object """
        # Overload the 'str()' operator to return the element's name
        return self.name


    def __lt__(self, other: Any) -> bool:
        """ Compare two Element object, using their name values """
        # Overload of the '<' operator to allow list sorting
        if type(other) != Element:
            return NotImplemented

        # Compare their name values and return a boolean
        if self.name < other.name:
            return True
        return False


    def reveal(self) -> None:
        """ Reveal this object, making it usable in-game """
        # Manages lists changes when a new element is revealed
        if not self.revealed:
            self.revealed = True
            ElementsCreated[self.name] = self
            del ElementsNotCreated[self.name]


    def initialize(self) -> None:
        """ Initialize the recipes list of the object """
        self.recipes = eval(self.recipes)



# Defining lists to allow indexing of all elements/groups
Elements = {}
ElementsCreated = {}
ElementsNotCreated = {}
Groups = {}



""" Creation of the instances of each objects, in order to set up game logic """

# Groups
Ignis = Group("Ignis")
Aqua = Group("Aqua")
Terra = Group("Terra")
Aer = Group("Aer")
Fulgur = Group("Fulgur")
Primus = Group("Primus")
Vitae = Group("Vitae")
Locus = Group("Locus")


# Base Elements
Fire = Element("Fire", "{}", Primus, True)
Air = Element("Air", "{}", Primus, True)
Water = Element("Water", "{}", Primus, True)
Earth = Element("Earth", "{}", Primus, True)
Energy = Element("Energy", "{}", Primus, True)
Void = Element("Void", "{}", Primus, True)


# 1st Level Compounds
Plasma = Element("Plasma", "{Fire, Energy}", Ignis)
Electricity = Element("Electricity", "{Air, Energy}", Fulgur)
Lava = Element("Lava", "{Fire, Earth}", Ignis)
Steam = Element("Steam", "{Air, Water}", Aer)
Heat = Element("Heat", "{Fire, Fire}", Primus)
Pressure = Element("Pressure", "{Earth, Energy}", Primus)
Sea = Element("Sea", "{Water, Water}", Aqua)
Wave = Element("Wave", "{Water, Energy}", Primus)
Wind = Element("Wind", "{Air, Air}", Aer)
Space = Element("Space", "{Void, Energy}", Primus)


# 2nd and Higher Level General Compounds
Sound = Element("Sound", "{Air, Wave}", Aer)
Ocean = Element("Ocean", "{Sea, Sea}", Aqua)
Salt = Element("Salt", "{Sea, Heat}", Terra)
Tsunami = Element("Tsunami", "{Sea, Wave}", Aqua)
Gravity = Element("Gravity", "{Pressure, Planet}", Primus)
Time = Element("Time", "{Gravity, Space}", Primus)
Explosion = Element("Explosion", "{Steam, Fire}", Ignis)


# Celestial Series
Cloud = Element("Cloud", "{Steam, Steam}", Aer)
Sky = Element("Sky", "{Cloud, Air}", Aer)
Tornado = Element("Tornado", "{Wind, Wind}", Aer)
Rain = Element("Rain", "{Cloud, Water}", Aqua)
Thunder = Element("Thunder", "{Cloud, Electricity}", Fulgur)
Hurricane = Element("Hurricane", "{Tornado, Tornado}", Aer)
Storm = Element("Storm", "{Thunder, Rain}", Fulgur)
LightningRod = Element("Lightning Rod", "{Thunder, Copper}", Fulgur)


# Mineral Series
Stone = Element("Stone", "{Lava, Air}", Terra)
Obsidian = Element("Obsidian", "{Lava, Water}", Terra)
Iron = Element("Iron", "{Stone, Pressure}", Terra)
Steel = Element("Steel", "{Iron, Heat}", Terra)
Coal = Element("Coal", "{Stone, Fire}", Terra)
Diamond = Element("Diamond", "{Coal, Pressure}", Terra)
Rust = Element("Rust", "{Iron, Water}", Terra)
Copper = Element("Copper", "{Iron, Stone}", Terra)
Tin = Element("Tin", "{Iron, Fire}", Terra)
Bronze = Element("Bronze", "{Copper, Tin}", Terra)


# Life Series
Cell = Element("Cell", "{Energy, Ocean}", Vitae)
Bacteria = Element("Bacteria", "{Cell, Cell}", Vitae)
Life = Element("Life", "{Bacteria, Energy}", Primus)
Worm = Element("Worm", "{Bacteria, Earth}", Vitae)
Soil = Element("Soil", "{Earth, Worm}", Terra)
Fish = Element("Fish", "{Bacteria, Sea}", Vitae)
Seed = Element("Seed", "{Soil, Life}", Vitae)
Grass = Element("Grass", "{Earth, Seed}", Vitae)
Plant = Element("Plant", "{Seed, Life}", Vitae)
Tree = Element("Tree", "{Plant, Life}", Vitae)
Forest = Element("Forest", "{Tree, Tree}", Vitae)


# Galactic Series
Star = Element("Star", "{Plasma, Void}", Locus)
BlackHole = Element("Black Hole", "{Void, Star}", Locus)
Pulsar = Element("Pulsar", "{Star, Electricity}", Locus)
Planet = Element("Planet", "{Stone, Void}", Locus)
OceanicPlanet = Element("Oceanic Planet", "{Planet, Ocean}", Locus)
Magma = Element("Magma", "{Planet, Lava}", Ignis)
SolarSystem = Element("Solar System", "{Planet, Star}", Locus)
Galaxy = Element("Galaxy", "{SolarSystem, BlackHole}", Locus)
LocalGroup = Element("Local Group", "{Galaxy, Galaxy}", Locus)
Universe = Element("Universe", "{LocalGroup, LocalGroup}", Locus)



# Sorts all of the groups' elements list, as a cleanup
Groups = {i: Groups[i] for i in sorted(Groups.keys())}
for i in Groups:
    Groups[i].elements.sort()


# Initialize all of the elements' recipes
for i in Elements:
    Elements[i].initialize()



""" Save file system """

# Defining two functions to allow encoding and decoding for the save file
def encode(strToEncode: str) -> str:
    """ Take a string and return its encoded version """
    # Uses a single-line for instruction to manually convert each character to
    # hexadecimal and apply a sequence of operations
    return "".join([str(hex((ord(n) * 2 + 3) * 7)) for n in strToEncode])

def decode(strToDecode: str) -> str:
    """ Take an encoded string and return its original """
    # Uses a single-line for instruction to manually convert each character back to Unicode
    return chr((int(strToDecode, 16) // 7 - 3) // 2)


# Handle the save file if present
try:
    with open("Elemental.save", "r") as f:
        # Read the save file and decode it
        toRead = f.read().split("0x")[1:]
        for j in ''.join([decode(i) for i in toRead]).split("\n")[:-1]:
            # Reveal each element one by one
            Elements[j].reveal()
except FileNotFoundError:
    # If no savefile is present, ignore
    pass
except:
    print("Corrupted savefile!\n")



""" GUI """

# Define the main window
main = tk.Tk()
main.title("Elemental")


# Define the console outputting text
console = tk.Frame(borderwidth=3, relief="sunken", background="white")
console.grid(row=1, column=0, columnspan=5, sticky="news")

logText = ["Welcome to Elemental!", "To create new elements, select one from both colums...", "And then, click the Fuse button!", ""]
consoleText = tk.Label(master=console, text="\n".join(logText[-4:-1] + [logText[-1]]), background="white")
consoleText.pack()



# Define three functions to handle selecting a group
group1 = list(Groups)[0]
group2 = list(Groups)[0]
def selectGroup1(selection: Tuple[int, ...]) -> None:
    global group1
    group1 = list([Groups[i] for i in Groups if Groups[i].isOnlyNonReveal()])[selection[0]]
    listboxElements1 = tk.StringVar(value=list([i for i in group1.elements if i.revealed]))
    listElements1["listvariable"] = listboxElements1

def selectGroup2(selection: Tuple[int, ...]) -> None:
    global group2
    group2 = list([Groups[i] for i in Groups if Groups[i].isOnlyNonReveal()])[selection[0]]
    listboxElements2 = tk.StringVar(value=list([i for i in group2.elements if i.revealed]))
    listElements2["listvariable"] = listboxElements2


def actualizeGroups() -> None:
    global group1, group2
    listGroups1["listvariable"] = tk.StringVar(value=list([Groups[i] for i in Groups if Groups[i].isOnlyNonReveal()]))
    listGroups2["listvariable"] = tk.StringVar(value=list([Groups[i] for i in Groups if Groups[i].isOnlyNonReveal()]))
    listboxElements1 = tk.StringVar(value=list([i for i in group1.elements if i.revealed]))
    listElements1["listvariable"] = listboxElements1
    listboxElements2 = tk.StringVar(value=list([i for i in group2.elements if i.revealed]))
    listElements2["listvariable"] = listboxElements2


# Define a function to handle selecting an element
element1 = 0
element2 = 0
def selectElement1(selection1) -> None:
    global element1, element2, group1, group2
    elementGroup1 = [i for i in group1.elements if i.revealed]
    element1 = elementGroup1[selection1[0]]
    spacesToAdd1 = max([len(i) for i in Elements]) - len(element1.name) + 1
    if not isinstance(element2, int):
        spacesToAdd2 = max([len(i) for i in Elements]) - len(element2.name) + 1
        fusionPreview["text"] = " " * spacesToAdd1 + "{} + {}".format(element1.name, element2.name) + " " * spacesToAdd2
    else:
        spacesToAdd2 = max([len(i) for i in Elements]) + 1
        fusionPreview["text"] = " " * spacesToAdd1 + "{} + ".format(element1.name) + " " * spacesToAdd2

def selectElement2(selection2) -> None:
    global element1, element2, group1, group2
    elementGroup2 = [i for i in group2.elements if i.revealed]
    element2 = elementGroup2[selection2[0]]
    spacesToAdd2 = max([len(i) for i in Elements]) - len(element2.name) + 1
    if not isinstance(element1, int):
        spacesToAdd1 = max([len(i) for i in Elements]) - len(element1.name) + 1
        fusionPreview["text"] = " " * spacesToAdd1 + "{} + {}".format(element1.name, element2.name) + " " * spacesToAdd2
    else:
        spacesToAdd1 = max([len(i) for i in Elements]) + 1
        fusionPreview["text"] = " " * spacesToAdd1 + " + {}".format( element2.name) + " " * spacesToAdd2


# Define the two groups selection lists
listboxGroups1 = tk.StringVar(value=list([Groups[i] for i in Groups if Groups[i].isOnlyNonReveal()]))
listGroups1 = tk.Listbox(listvariable=listboxGroups1)
listGroups1.grid(row=0, column=0, sticky="news")
listGroups1.bind("<Double-1>", lambda e: selectGroup1(listGroups1.curselection()))

listboxGroups2 = tk.StringVar(value=list([Groups[i] for i in Groups if Groups[i].isOnlyNonReveal()]))
listGroups2 = tk.Listbox(listvariable=listboxGroups2)
listGroups2.grid(row=0, column=4, sticky="news")
listGroups2.bind("<Double-1>", lambda e: selectGroup2(listGroups2.curselection()))


# Define the two elements selection lists
listElements1 = tk.Listbox()
listElements1.grid(row=0, column=1, sticky="news")
listElements1.bind("<Double-1>", lambda e: selectElement1(listElements1.curselection()))

listElements2 = tk.Listbox()
listElements2.grid(row=0, column=3, sticky="news")
listElements2.bind("<Double-1>", lambda e: selectElement2(listElements2.curselection()))




# Define the fuse function for the Fuse button
def fuse() -> None:
    # Pull the global variables
    global element1, element2, consoleText, logText
    # Test if two elements were selected
    if element1 != 0 and element2 != 0:
        # Obtain a dictionary out of the two fused elements
        fusion = {element1, element2}
        newElement = False

        # Test for each element
        for i in list(Elements):
            if fusion == Elements[i].recipes:
                # If match is found and element not revealed
                if not Elements[i].revealed:
                    # Reveal the element and inform the player
                    newElement = True
                    logText.append("Created Element {}!".format(str(Elements[i])))
                    consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])
                    Elements[i].reveal()
                    actualizeGroups()
                # If match is found and element already revealed
                else:
                    # Inform the player
                    newElement = True
                    logText.append("Element {} already created".format(str(Elements[i])))
                    consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])

        # If no match were found, inform the player
        if not newElement:
            logText.append("No new Element created...")
            consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])
    
    else:
        # Send the error message
        logText.append("Please select two elements")
        consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])


# Define the Fuse button + fusion preview text
fusionGroup = tk.Frame()
fusionGroup.grid(row=0, column=2)

spacesToAdd = max([len(i) for i in Elements]) + 1
fusionPreview = tk.Label(text=" " * spacesToAdd + " + " + " " * spacesToAdd, master=fusionGroup, font="TkFixedFont")
fusionPreview.pack()

fusionButton = tk.Button(text="Fuse", master=fusionGroup, command=fuse)
fusionButton.pack()


# Handle the row and column rescaling
rowWeights = [1, 2]
[main.columnconfigure(i, weight=1) for i in range(5)]
main.rowconfigure(0, weight=1)


# Start the window
main.mainloop()


# When the window is closed, save data into a savefile
with open("Elemental.save", "wt") as f:
    for i in ElementsCreated:
        # Write each encoded element into the savefile
        toWrite = encode(str(i) + "\n")
        f.write(toWrite)