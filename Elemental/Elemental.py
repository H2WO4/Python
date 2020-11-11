""" Importing Ressources """

import tkinter as tk
from ElementData import Elements, ElementsCreated, ElementsNotCreated, Groups



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
    with open("Elemental.save", "r") as f:
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

def selectGroup1(selection):
    print(selection)


def selectGroup2(selection):
    print(selection)

def selectElement(selection1, selection2):
    fusionPreview["text"] = "{} + {}".format(list(Elements)[selection1], list(Elements)[selection2])



main = tk.Tk()
main.title("Elemental")
title = tk.Label(text="Elemental")
title.grid(row=0, column=2)



listboxGroups1 = tk.StringVar(value=list(Groups))
listGroups1 = tk.Listbox(listvariable=listboxGroups1, height=len(Groups))
listGroups1.grid(row=1, column=0)
listGroups1.bind("<Double-1>", lambda e: selectGroup1(listGroups1.curselection()))

listboxElements1 = tk.StringVar(value=list(Elements))
listElements1 = tk.Listbox(listvariable=listboxElements1, height=len(Groups))
listElements1.grid(row=1, column=1)
listElements1.bind("<Double-1>", lambda e: selectElement(listElements1.curselection()[-1], listElements2.curselection()[-1]))


listboxGroups2 = tk.StringVar(value=list(Groups))
listGroups2 = tk.Listbox(listvariable=listboxGroups2, height=len(Groups))
listGroups2.grid(row=1, column=4)
listGroups2.bind("<Double-1>", lambda e: selectGroup2(listGroups2.curselection()))

listboxElements2 = tk.StringVar(value=list(Elements))
listElements2 = tk.Listbox(listvariable=listboxElements2, height=len(Groups))
listElements2.grid(row=1, column=3)
listElements2.bind("<Double-1>", lambda e: selectElement(listElements1.curselection()[-1], listElements2.curselection()[-1]))



fusionGroup = tk.Frame()
fusionGroup.grid(row=1, column=2)

fusionPreview = tk.Label(text="Air + Air", master=fusionGroup)
fusionPreview.pack()

fusionButton = tk.Button(text="Fuse", master=fusionGroup)
fusionButton.pack()



rowWeights = [0, 1]
[main.columnconfigure(i, weight=1) for i in range(5)]
[main.rowconfigure(i, weight=rowWeights[i]) for i in range(2)]


main.mainloop()



""" Main game loop """

# Display welcome text
print("Welcome to Elemental !\n")
print("The rules are simple :\nUse all the elements to your disposition to create new ones.")
print("For more detailed help, type \"help\".\n")

leave = True
while not leave:

    command = input().lower()

    if command in {"group", "groups"}:
        # Print all elements in a group

        print("\nWhich group do you want to look at?")
        for i in Groups:
            # Print every group
            print(i)

        try:
            command = input("\n").title()

            if command in Groups:
                print("\n{} Group:".format(str(command)))

                for i in Groups[command].elements:
                    # Enumerate every revealed element in the group
                    if i.revealed:
                        print(i)

        # Error handling for incorrect name for group
        except ZeroDivisionError:
            print("Incorrect group name!")
                
    elif command in {"fuse", "fusion", "mix"}:
        # Handle fusing elements

        try:
            # Gather two text inputs and verify their validity
            reactif1 = input("\nChoose a first element : ").title()
            if not reactif1 in ElementsCreated:
                raise IndexError
            reactif2 = input("\nChoose a second element : ").title()
            if not reactif2 in ElementsCreated:
                raise IndexError

            # Put them in a single variable and evaluate it to transform it into a set
            command = eval("{} + {}".format("Elements[reactif1]", "Elements[reactif2]"))
            newElement = False

            # Iterate through the entire element list to find a match
            for i in list(ElementsNotCreated):
                if command in ElementsNotCreated[i]:
                    # Reveal the created element
                    newElement = True
                    print("\nCreated Element {}!".format(str(ElementsNotCreated[i])))
                    ElementsNotCreated[i].reveal()
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
        print("In order to obtain new elements, type \"fuse\", then enter the two elements that you want to try fusing.\n")
        print("To stop the program, type \"leave\", your progress will be saved into a savefile.")

    elif command in {"leave", "close", "leave"}:
        # Handle program exit

        leave = True

    elif command in {"reveal"}:
        # Testing instruction - Reveal all elements

        ElementsNotCreatedCopy = ElementsNotCreated.copy()
        for i in ElementsNotCreatedCopy:
            print(ElementsNotCreatedCopy[i])
            ElementsNotCreatedCopy[i].reveal()

    # Adds a newline between user instructions
    print("")

# Save data into a savefile
with open("Elemental.save", "wt") as f:
    for i in ElementsCreated:
        # Write each encoded element into the savefile
        toWrite = encode(str(i) + "\n")
        f.write(toWrite)