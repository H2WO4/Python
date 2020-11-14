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
    spacesToAdd1 = max([len(i) for i in Elements]) - len(group1.elements[element1].name) + 1
    spacesToAdd2 = max([len(i) for i in Elements]) - len(group2.elements[element2].name) + 1
    fusionPreview["text"] = " " * spacesToAdd1 + "{} + {}".format(group1.elements[element1], group2.elements[element2]) + " " * spacesToAdd2


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
    global group1, group2, element1, element2
    # Put them in a single variable and evaluate it to transform it into a set
    fusion = {group1.elements[element1], group2.elements[element2]}
    newElement = False
    # Iterate through the entire element list to find a match
    for i in list(ElementsNotCreated):
        if fusion in ElementsNotCreated[i]:
            # Reveal the created element
            newElement = True
            print("\nCreated Element {}!".format(str(ElementsNotCreated[i])))
            ElementsNotCreated[i].reveal()
    if not newElement:
        print("\nNo new element created...")


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



""" Main game loop """
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