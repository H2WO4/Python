""" Importing Ressources """

import tkinter as tk

""" Object Definition """

class Element:
    """
    The Element object is used to represent a singular element\n
    It contains information about its name, in which group it belongs,
    its state and the list of its recipes
    """

    def __init__(self, name, recipes, group = None, revealed = False):
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

    def __str__(self):
        """ Return the name value of the object """
        # Overload the 'str()' operator to return the element's name
        return self.name

    def __contains__(self, other):
        """ Check if a set of two Element objects is present within a third Element recipes list """
        # Overload of the 'in' operator to perform inclusion logic check during element fusion
        if type(other) != set:
            return NotImplemented

        # Search for the set in the elements recipes and return a boolean
        if other in self.recipes:
            return True
        return False

    def __add__(self, other):
        """ Add two Elements object to themselves, putting them into an unordered set """
        # Overload of the '+' operator to set up element fusion
        if type(other) != Element:
            return NotImplemented

        # Return a set containing the two elements
        return {self, other}

    def __lt__(self, other):
        """ Compare two Element object, using their name values """
        # Overload of the '<' operator to allow list sorting
        if type(other) != Element:
            return NotImplemented

        # Compare their name values and return a boolean
        if self.name < other.name:
            return True
        return False

    def reveal(self):
        """ Reveal this object, making it usable in-game """
        # Manages lists changes when a new element is revealed
        if not self.revealed:
            self.revealed = True
            ElementsCreated[self.name] = self
            del ElementsNotCreated[self.name]

        return None

    def initialize(self):
        """ Initialize the recipes list of the object """
        self.recipes = eval(self.recipes)

        return None


class Group:
    """
    The Group object is used to represent a list of elements\n
    It contains information about its name, as well as an ordered list of its members
    """

    def __init__(self, name):
        """ Initialize a Group object """
        # Init - Setting attributes
        self.name = name
        self.elements = []

        # Init - Adding itself to lists for future indexing
        Groups[self.name] = self

    def __str__(self):
        """ Return the name value of the object """
        # Overload the 'str()' operator to return the group's name
        return self.name



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
Vitae = Group("Vitae")
Primus = Group("Primus")
Locus = Group("Locus")


# Base Elements
Fire = Element("Fire", "[]", Ignis, True)
Air = Element("Air", "[]", Aer, True)
Water = Element("Water", "[]", Aqua, True)
Earth = Element("Earth", "[]", Terra, True)
Energy = Element("Energy", "[]", Primus, True)
Void = Element("Void", "[]", Primus, True)

# 1st Level Compounds
Plasma = Element("Plasma", "[Fire + Energy]", Ignis)
Electricity = Element("Electricity", "[Air + Energy]", Fulgur)
Lava = Element("Lava", "[Fire + Earth]", Ignis)
Steam = Element("Steam", "[Air + Water]", Aer)
Heat = Element("Heat", "[Fire + Fire]", Primus)
Pressure = Element("Pressure", "[Earth + Energy]", Primus)
Stone = Element("Stone", "[Earth + Earth]", Terra)
Sea = Element("Sea", "[Water + Water]", Aqua)
Wave = Element("Wave", "[Water + Energy]", Primus)
Wind = Element("Wind", "[Air + Air]", Aer)
Space = Element("Space", "[Void + Energy]", Primus)

# 2nd and Higher Level General Compounds
Sound = Element("Sound", "[Air + Wave]", Aer)
Ocean = Element("Ocean", "[Sea + Sea]", Aqua)
Salt = Element("Salt", "[Sea + Heat]", Terra)
Tsunami = Element("Tsunami", "[Sea + Wave]", Aqua)
Gravity = Element("Gravity", "[Pressure + Planet]", Primus)
Time = Element("Time", "[Gravity + Space]", Primus)

# Celestial Series
Cloud = Element("Cloud", "[Steam + Steam]", Aer)
Sky = Element("Sky", "[Cloud + Air]", Aer)
Tornado = Element("Tornado", "[Wind + Wind]", Aer)
Rain = Element("Rain", "[Cloud + Water]", Aqua)
Thunder = Element("Thunder", "[Cloud + Electricity]", Fulgur)
Hurricane = Element("Hurricane", "[Tornado + Tornado]", Aer)

# Mineral Series
Obsidian = Element("Obsidian", "[Lava + Water]", Terra)
Iron = Element("Iron", "[Stone + Pressure]", Terra)
Steel = Element("Steel", "[Iron + Heat]", Terra)
Coal = Element("Coal", "[Stone + Fire]", Terra)
Diamond = Element("Diamond", "[Coal + Pressure]", Terra)
Rust = Element("Rust", "[Iron + Water]", Terra)
Copper = Element("Copper", "[Iron + Stone]", Terra)
Tin = Element("Tin", "[Iron + Fire]", Terra)
Bronze = Element("Bronze", "[Copper + Tin]", Terra)

# Life Series
Cell = Element("Cell", "[Energy + Ocean]", Vitae)
Bacteria = Element("Bacteria", "[Cell + Cell]", Vitae)
Life = Element("Life", "[Bacteria + Energy]", Primus)
Worm = Element("Worm", "[Bacteria + Earth]", Vitae)
Soil = Element("Soil", "[Earth + Worm]", Terra)
Fish = Element("Fish", "[Bacteria + Sea]", Vitae)
Seed = Element("Seed", "[Soil + Life]", Vitae)
Grass = Element("Grass", "[Earth + Seed]", Vitae)
Plant = Element("Plant", "[Seed + Life]", Vitae)

# Galactic Series
Star = Element("Star", "[Plasma + Void]", Locus)
BlackHole = Element("Black Hole", "[Void + Star]", Locus)
Pulsar = Element("Pulsar", "[Star + Electricity]", Locus)
Planet = Element("Planet", "[Stone + Void]", Locus)
OceanicPlanet = Element("Oceanic Planet", "[Planet + Ocean]", Locus)
Magma = Element("Magma", "[Planet + Lava]", Ignis)
SolarSystem = Element("Solar System", "[Planet + Star]", Locus)
Galaxy = Element("Galaxy", "[SolarSystem + BlackHole]", Locus)
LocalGroup = Element("Local Group", "[Galaxy + Galaxy]", Locus)
Universe = Element("Universe", "[LocalGroup + LocalGroup]", Locus)


Groups = {i: Groups[i] for i in sorted(Groups.keys())}
# Sorts all of the groups' elements list, as a cleanup
for i in Groups:
    Groups[i].elements.sort()

# Initialize all of the elements' recipes
for i in Elements:
    Elements[i].initialize()

""" Save file system """

# Defining two functions to allow encoding and decoding for the save file
def encode(strToEncode):
    """ Take a string and return its encoded version """
    # Uses a single-line for instruction to manually convert each character to
    # hexadecimal and apply a sequence of operations
    return ''.join([str(hex((ord(n) * 2 + 3) * 7)) for n in strToEncode])

def decode(strToDecode):
    """ Take an encoded string and return its original """
    # Uses a single-line for instruction to manually convert each character back to Unicode
    return chr((int(strToDecode, 16) // 7 - 3) // 2)


# Handle the save file if present
try:
    with open("Elemental/Elemental.save", "r") as f:
        # Read the save file and decode it
        toRead = f.read().split("0x")[1:]
        for j in ''.join([decode(i) for i in toRead]).split("\n")[:-1]:
            # Reveal each element one by one
            Elements[j].reveal()
except FileNotFoundError:
    # If no savefile is present, ignore
    pass
except ZeroDivisionError:
    print("Corrupted savefile!\n")



""" GUI """

main = tk.Tk()
main.title("Elemental")
title = tk.Label(text="Elemental")
title.grid(row=0, column=2)




console = tk.Frame(borderwidth=3, relief="sunken", background="white")
console.grid(row=2, column=0, columnspan=5, sticky="news")

logText = ["", "", "", ""]
consoleText = tk.Label(master=console, text="\n".join(logText[-4:-1] + [logText[-1]]), background="white")
consoleText.pack()




group1 = list(Groups)[0]
group2 = list(Groups)[0]
def selectGroup1(selection):
    global group1, logText, consoleText
    group1 = Groups[list(Groups)[selection[0]]]
    listboxElements1 = tk.StringVar(value=list([i for i in group1.elements if i.revealed]))
    listElements1["listvariable"] = listboxElements1


def selectGroup2(selection):
    global group2
    group2 = Groups[list(Groups)[selection[0]]]
    listboxElements2 = tk.StringVar(value=list([i for i in group2.elements if i.revealed]))
    listElements2["listvariable"] = listboxElements2


element1 = 0
element2 = 0
def selectElement(selection1, selection2):
    global element1, element2
    if len(selection1) > 0:
        element1 = selection1[0]
    if len(selection2) > 0:
        element2 = selection2[0]
    elementGroup1 = [i for i in group1.elements if i.revealed]
    elementGroup2 = [i for i in group2.elements if i.revealed]
    spacesToAdd1 = max([len(i) for i in Elements]) - len(elementGroup1[element1].name) + 1
    spacesToAdd2 = max([len(i) for i in Elements]) - len(elementGroup2[element2].name) + 1
    fusionPreview["text"] = " " * spacesToAdd1 + "{} + {}".format(elementGroup1[element1], elementGroup2[element2]) + " " * spacesToAdd2


listboxGroups1 = tk.StringVar(value=list(Groups))
listGroups1 = tk.Listbox(listvariable=listboxGroups1)
listGroups1.grid(row=1, column=0, sticky="news")
listGroups1.bind("<Double-1>", lambda e: selectGroup1(listGroups1.curselection()))

listElements1 = tk.Listbox()
listElements1.grid(row=1, column=1, sticky="news")
listElements1.bind("<Double-1>", lambda e: selectElement(listElements1.curselection(), listElements2.curselection()))
selectGroup1((0, ))


listboxGroups2 = tk.StringVar(value=list(Groups))
listGroups2 = tk.Listbox(listvariable=listboxGroups2)
listGroups2.grid(row=1, column=4, sticky="news")
listGroups2.bind("<Double-1>", lambda e: selectGroup2(listGroups2.curselection()))

listElements2 = tk.Listbox()
listElements2.grid(row=1, column=3, sticky="news")
listElements2.bind("<Double-1>", lambda e: selectElement(listElements1.curselection(), listElements2.curselection()))
selectGroup2((0, ))




def fuse():
    global group1, group2, element1, element2, consoleText, logText
    elementGroup1 = [i for i in group1.elements if i.revealed]
    elementGroup2 = [i for i in group2.elements if i.revealed]

    fusion = {elementGroup1[element1], elementGroup2[element2]}
    newElement = False

    for i in list(ElementsNotCreated):
        if fusion in ElementsNotCreated[i]:
            newElement = True
            logText.append("Created Element {}!".format(str(ElementsNotCreated[i])))
            consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])
            ElementsNotCreated[i].reveal()
    if not newElement:
        logText.append("No new Element created ...")
        consoleText["text"] = "\n".join(logText[-4:-1] + [logText[-1]])


fusionGroup = tk.Frame()
fusionGroup.grid(row=1, column=2)

spacesToAdd = max([len(i) for i in Elements]) + 1
fusionPreview = tk.Label(text=" " * spacesToAdd + " + " + " " * spacesToAdd, master=fusionGroup, font="TkFixedFont")
fusionPreview.pack()

fusionButton = tk.Button(text="Fuse", master=fusionGroup, command=fuse)

fusionButton.pack()


rowWeights = [0, 1, 2]
[main.columnconfigure(i, weight=1) for i in range(5)]
[main.rowconfigure(i, weight=rowWeights[i]) for i in range(3)]


main.mainloop()


# Save data into a savefile
with open("Elemental/Elemental.save", "wt") as f:
    for i in ElementsCreated:
        # Write each encoded element into the savefile
        toWrite = encode(str(i) + "\n")
        f.write(toWrite)