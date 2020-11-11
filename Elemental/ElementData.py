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
Wind = Element("Wind", "[Air + Energy]", Aer)
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