class Element:
    def __init__(self, name, recipes, group = None, revealed = False):
        self.name = name
        self.recipes = recipes
        self.group = group
        self.revealed = revealed

        Elements.append(self)
        if group != None:
            group.elements.append(self)
        
        if revealed:
            ElementsCreated.append(self)
        else:
            ElementsNotCreated.append(self)
    
    def __str__(self):
        return self.name

    def __contains__(self, other):
        if type(other) != list:
            raise TypeError
        if other in self.recipes:
            return True
        else:
            other.reverse()
            if other in self.recipes:
                return True
            else:
                return False
    
    def __add__(self, other):
        if type(other) != Element:
            raise TypeError
        return [self, other]
    
    def __lt__(self, other):
        if type(other) != Element:
            raise TypeError
        
        if self.name < other.name:
            return True
        else:
            return False
    
    def reveal(self):
        if not self.revealed:
            self.revealed = True
            ElementsCreated.append(self)
            ElementsCreated.sort()
            ElementsNotCreated.pop(ElementsNotCreated.index(self))


class Group:
    def __init__(self, name):
        self.name = name
        self.elements = []
        Groups.append(self)
    
    def __str__(self):
        return self.name

    def __iadd__(self, other):
        if type(other) != Element:
            raise TypeError
        self.elements.append(other)



Elements = []
ElementsCreated = []
ElementsNotCreated = []
Groups = []

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
Fire = Element("Fire", [], Ignis, True)
Air = Element("Air", [], Aer, True)
Water = Element("Water", [], Aqua, True)
Earth = Element("Earth", [], Terra, True)
Energy = Element("Energy", [], Primus, True)
Void = Element("Void", [], Primus, True)

# 1st Level Compounds
Plasma = Element("Plasma", [Fire + Energy], Ignis)
Electricity = Element("Electricity", [Air + Energy], Fulgur)
Lava = Element("Lava", [Fire + Earth], Ignis)
Steam = Element("Steam", [Air + Water], Aer)
Heat = Element("Heat", [Fire + Fire], Primus)
Pressure = Element("Pressure", [Earth + Energy], Primus)
Stone = Element("Stone", [Earth + Earth], Terra)
Sea = Element("Sea", [Water + Water], Aqua)
Wave = Element("Wave", [Water + Energy], Primus)
Wind = Element("Wind", [Air + Energy], Aer)

# 2nd and Higher Level General Compounds
Sound = Element("Sound", [Air + Wave], Aer)
Ocean = Element("Ocean", [Sea + Sea], Aqua)
Salt = Element("Salt", [Sea + Heat], Terra)
Tsunami = Element("Tsunami", [Sea + Wave], Aqua)

# Celestial Series
Cloud = Element("Cloud", [Steam + Steam], Aer)
Tornado = Element("Tornado", [Wind + Wind], Aer)
Rain = Element("Rain", [Cloud + Water], Aqua)
Thunder = Element("Thunder", [Cloud + Electricity], Fulgur)
Hurricane = Element("Hurricane", [Tornado + Tornado], Aer)

# Mineral Series
Obsidian = Element("Obsidian", [Lava + Water], Terra)
Iron = Element("Iron", [Stone + Pressure], Terra)
Steel = Element("Steel", [Iron + Heat], Terra)
Coal = Element("Coal", [Stone + Fire], Terra)
Diamond = Element("Diamond", [Coal + Pressure], Terra)
Rust = Element("Rust", [Iron + Water], Terra)
Copper = Element("Copper", [Iron + Stone], Terra)
Tin = Element("Tin", [Iron + Fire], Terra)
Bronze = Element("Bronze", [Copper + Tin], Terra)

# Life Series
Cell = Element("Cell", [Energy + Ocean], Vitae)
Bacteria = Element("Bacteria", [Cell + Cell], Vitae)
Life = Element("Life", [Bacteria + Energy], Primus)
Worm = Element("Worm", [Bacteria + Earth], Vitae)
Soil = Element("Soil", [Earth + Worm], Terra)
Fish = Element("Fish", [Bacteria + Sea], Vitae)

# Galactic Series
Star = Element("Star", [Plasma + Void], Locus)
BlackHole = Element("Black Hole", [Void + Star], Locus)
Pulsar = Element("Pulsar", [Star + Electricity], Locus)
Planet = Element("Planet", [Stone + Void], Locus)
OceanicPlanet = Element("Oceanic Planet", [Planet + Ocean], Locus)
Magma = Element("Magma", [Planet + Lava], Ignis)
SolarSystem = Element("Solar System", [Planet + Star], Locus)



for i in Groups:
    i.elements.sort()

try:
    with open("ElementSave.txt", "r") as f:
        toRead = f.read().split("\n")[:-1]
        for i in toRead:
            eval(i.replace(" ", "")).reveal()
except FileNotFoundError:
    pass

quit = False
while not quit:
    command = input("\n").lower()
    if command in ["group", "groups"]:
        print("\nWhich group do you want to look at?")
        for i in Groups:
            print(i)
        command = eval(input("\n").title())
        if command in Groups:
            print("\n" + str(command) + " Group:")
            for i in command.elements:
                if i.revealed:
                    print(str(i))
                
    elif command in ["fuse", "fusion", "mix"]:
        try:
            if not (reactif1 := eval(input("\nChoose a first element : ").title())) in ElementsCreated:
                raise IndexError
            if not (reactif2 := eval(input("\nChoose a first element : ").title())) in ElementsCreated:
                raise IndexError

            command = eval("{} + {}".format(reactif1, reactif2))
            newElement = False
            for i in ElementsNotCreated:
                if command in i:
                    newElement = True
                    print("\nCreated Element {}!".format(str(i)))
                    i.reveal()
            if not newElement:
                print("No new element created")
        except NameError:
            print("\nInexisting element name!")
        except IndexError:
            print("\nNon-Discovered element!")
    
    elif command in ["list"]:
        print("\nElement list :")
        for i in ElementsCreated:
            print(i)

    elif command in ["quit", "close", "leave"]:
        quit = True
    
    elif command in ["reveal"]:
        ElementsNotCreatedCopy = []
        for i in ElementsNotCreated:
            ElementsNotCreatedCopy.append(i)
        for i in ElementsNotCreatedCopy:
            print(i)
            i.reveal()

with open("ElementSave.txt", "w") as f:
    for i in ElementsCreated:
        f.write(str(i) + "\n")