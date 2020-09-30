""" Object Definition """

class Element:
    """
    The Element object is used to represent a singular element\n
    It contains information about its name, in which group it belongs, its state and the list of its recipes
    """

    def __init__(self, name, recipes, group = None, revealed = False):
        """ Initialize an Element object """
        # Init - Setting attributes
        self.name = name
        self.recipes = recipes
        self.group = group
        self.revealed = revealed

        # Init - Adding itself to lists for future indexing
        Elements.append(self)
        if group != None:
            group.elements.append(self)
        
        if revealed:
            ElementsCreated.append(self)
        else:
            ElementsNotCreated.append(self)
    
    def __str__(self):
        """ Return the name value of the object """
        # Overload the 'str()' operator to return the element's name
        return self.name

    def __contains__(self, other):
        """ Check if a set of two Element objects is present within a third Element recipes list """
        # Overload of the 'in' operator to perform inclusion logic check during element fusion
        if type(other) != set:
            raise TypeError

        # Search for the set in the elements recipes and return a boolean
        if other in self.recipes:
            return True
        return False
    
    def __add__(self, other):
        """ Add two Elements object to themselves, putting them into an unordered set """
        # Overload of the '+' operator to set up element fusion
        if type(other) != Element:
            raise TypeError

        # Return a set containing the two elements
        return {self, other}
    
    def __lt__(self, other):
        """ Compare two Element object, using their name values """
        # Overload of the '<' operator to allow list sorting
        if type(other) != Element:
            raise TypeError
        
        # Compare their name values and return a boolean
        if self.name < other.name:
            return True
        return False
    
    def reveal(self):
        """ Reveal this object, making it usable in-game """
        # Manages lists changes when a new element is revealed
        if not self.revealed:
            self.revealed = True
            ElementsCreated.append(self)
            ElementsCreated.sort()
            ElementsNotCreated.pop(ElementsNotCreated.index(self))
        
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
        Groups.append(self)
    
    def __str__(self):
        """ Return the name value of the object """
        # Overload the 'str()' operator to return the group's name
        return self.name

# Defining two functions to allow encoding and decoding for the save file
def encode(strToEncode):
    """ Take a string and return its encoded version """
    # Uses a single-line for instruction to manually convert each character to hexadecimal and apply a sequence of operations
    return ''.join([str(hex((ord(n) * 2 + 3) * 7)) for n in strToEncode])

def decode(strToDecode):
    """ Take an encoded string and return its original """
    # Uses a single-line for instruction to manually convert each character back to ASCII
    return chr((int(strToDecode, 16) // 7 - 3) // 2)

# Defining lists to allow indexing of all elements/groups
Elements = []
ElementsCreated = []
ElementsNotCreated = []
Groups = []

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

# 2nd and Higher Level General Compounds
Sound = Element("Sound", "[Air + Wave]", Aer)
Ocean = Element("Ocean", "[Sea + Sea]", Aqua)
Salt = Element("Salt", "[Sea + Heat]", Terra)
Tsunami = Element("Tsunami", "[Sea + Wave]", Aqua)
Gravity = Element("Gravity", "[Pressure + Planet]", Primus)

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


# Sorts all of the groups' elements list, as a cleanup
for i in Groups:
    i.elements.sort()

# Initialize all of the elements' recipes
for i in Elements:
    i.initialize()


""" Save file system """

# Handle the save file if present
try:
    with open("Elemental.save", "r") as f:
        # Read the save file and decode it
        toRead = f.read().split("0x")[1:]
        for j in ''.join([decode(i) for i in toRead]).split("\n")[:-1]:
            # Reveal each element one by one
            eval(j.replace(" ", "")).reveal()
except FileNotFoundError:
    pass
except:
    print("Corrupted savefile!\n")



""" Main game loop """

print("Welcome to Elemental !\n")
print("The rules are simple :\nUse all the elements to your disposition to create new ones.")
print("For more detailed help, type \"help\".\n")

quit = False
while not quit:

    command = input().lower()

    if command in {"group", "groups"}:
        # Print all elements in a group
        print("\nWhich group do you want to look at?")
        for i in Groups:
            # Print every group
            print(i)
        
        command = eval(input("\n").title())

        if command in Groups:
            print("\n{} Group:".format(str(command)))

            for i in command.elements:
                # Enumerate every revealed element in the group
                if i.revealed:
                    print(str(i))
                
    elif command in {"fuse", "fusion", "mix"}:
        # Handle fusing elements
        try:
            # Gather two text inputs and verify their validity
            if not (reactif1 := eval(input("\nChoose a first element : ").title())) in ElementsCreated:
                raise IndexError
            if not (reactif2 := eval(input("Choose a second element : ").title())) in ElementsCreated:
                raise IndexError

            # Put them in a single variable and evaluate it to transform it into a set
            command = eval("{} + {}".format(reactif1, reactif2))
            newElement = False

            # Iterate through the entire element list to find a match
            for i in ElementsNotCreated:
                if command in i:
                    # Reveal the created element
                    newElement = True
                    print("\nCreated Element {}!".format(str(i)))
                    i.reveal()
            if not newElement:
                print("\nNo new element created...")
        
        # Error handling for incorrect/invalid element name
        except NameError:
            print("\nInexisting element name!")
        except IndexError:
            print("\nNon-Discovered element!")
    
    elif command in {"list"}:
        # Print all currently revealed elements
        print("\nElement list :")
        for i in ElementsCreated:
            print(i)
    
    elif command in {"help"}:
        # Display help text
        print("\nIn order to obtain a complete list of discovered elements, type \"list\".")
        print("If you want to display only a specific group, type \"group\", and then enter the group name.\n")
        print("In order to obtain new elements, type \"fuse\", then enter the two elements that you want to fuse.\n")
        print("To stop the program, type \"quit\", your progress will be saved into a savefile.")

    elif command in {"quit", "close", "leave"}:
        # Handle program exit
        quit = True
    
    elif command in {"reveal"}:
        # Testing instruction - Reveal all elements
        ElementsNotCreatedCopy = []
        for i in ElementsNotCreated:
            ElementsNotCreatedCopy.append(i)
        for i in ElementsNotCreatedCopy:
            print(i)
            i.reveal()
    
    print("")

# Save data into a savefile
with open("Elemental.save", "w") as f:
    for i in ElementsCreated:
        # Write each encoded element into the savefile
        f.write(encode(str(i) + "\n"))