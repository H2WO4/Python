from typing import Any, Dict, List, Tuple, Union
import tkinter as tk

class Terrain:
    def __init__(self, name: str, ID: str, color: str, description: str) -> None:
        self.name = name
        self.color = color
        self.id = ID
        self.description = description

        TerrainList[self.id] = self
class Grid:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size * 2 + 1
        self.grid: List[List[Terrain]] = [[TerrainList["empty"] for j in range(size * 2 + 1)] for i in range(size * 2 + 1)]
    
    def __getitem__(self, key: Tuple[int, int]) -> Terrain:
        return self.grid[key[0]][key[1]]
    
    def __setitem__(self, key: Union[int, Tuple[int, int]], other) -> None:
        if isinstance(key, int):
            self.grid[key] = other
        else:
            self.grid[key[0]][key[1]] = other
class GridLabel(tk.Label):

    def __init__(self, x: int, y: int, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.bind("<Enter>", self.displayDescription)

    def displayDescription(self, _: Any) -> None:
        descriptionText["text"] = newGrid[self.x, self.y].name + 2 * "\n" + newGrid[self.x, self.y].description + "\n" + 100 * " "

TerrainList: Dict[str, Terrain] = {}

Empty = Terrain("Empty", "empty", "white", "")
Woods = Terrain("Woods", "woods", "green", "-1 Movement if starting turn here.\n+2 Defense if ending turn here.")
River = Terrain("River", "river", "cyan", "Passable only by foot, aerian and amphibian units.\nCost 3 Movement for foot units to cross.")
Desert = Terrain("Desert", "desert", "yellow", "-1 Defense if ending turn here.")


gridSize = 9

newGrid = Grid("A", gridSize//2)


""" Graphical Interface """


# Define the update function
def update() -> None:
    for i in range(gridSize):
        for j in range(gridSize):
            grid[i][j]["background"] = newGrid[i, j].color
            gridText[i][j]["background"] = newGrid[i, j].color


# Define the main window
main = tk.Tk()
main.title("Citylization")


# Define the console outputting text
console = tk.Frame(borderwidth=3, relief="sunken", background="white")
console.grid(row=gridSize+1, column=0, columnspan=gridSize, sticky="news")

logText = ["Welcome to Fire Emblem!", " " * 80, "", ""]
consoleText = tk.Label(master=console, text="\n".join(logText[-4:-1] + [logText[-1]]), background="white")
consoleText.pack()


# Define the main grid
grid: List[List[tk.Frame]] = []
gridText: List[List[GridLabel]] = []
for i in range(gridSize):
    grid.append([])
    gridText.append([])
    for j in range(gridSize):
        grid[i].append(tk.Frame(borderwidth=3, relief="ridge", background="white"))
        grid[i][j].grid(row=i, column=j, sticky="news")
        gridText[i].append(GridLabel(i, j, master=grid[i][j], text="", background="white"))
        gridText[i][j].pack()


# Define the description panel
descriptionPanel = tk.Frame(borderwidth=3, relief="sunken", background="white")
descriptionPanel.grid(row=0, column=gridSize+1, rowspan=gridSize, sticky="news")

descriptionText = tk.Label(master=descriptionPanel, text=" " * 100, background="white")
descriptionText.pack()


# Define the end turn button
endTurnGroup = tk.Frame()
endTurnGroup.grid(row=gridSize+1, column=gridSize+1)

endTurnButton = tk.Button(text="End Turn", master=endTurnGroup)
endTurnButton.pack()


# Setup windows resizing
[main.columnconfigure(i, weight=1) for i in range(gridSize)]
main.columnconfigure(gridSize+1, weight=4)
[main.rowconfigure(i, weight=1) for i in range(gridSize)]
main.rowconfigure(gridSize+1, weight=4)


# Tests
def test() -> None:
    newGrid[2, 2] = Woods
    for i in range(gridSize):
        newGrid[6, i] = River
    for i, j in ((4, 6), (4, 7), (4, 5), (5, 6)):
        newGrid[i, j] = Desert
    
    update()

# Start the window
test()
main.mainloop()