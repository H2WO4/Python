import tkinter as tk
from typing import Any, List, Tuple, Union

class Stack:
    def __init__(self, data: List[Any] = []) -> None:
        self.data = data
    
    def push(self, *others: Tuple[Any, ...]) -> None:
        self.data = list(others) + self.data
    
    def pull(self) -> Tuple[Any, ...]:
        out = self.data[0]
        self.data = self.data[1:]
        return out
    
    def peek(self) -> Any:
        return self.data[0]
    
    def __len__(self) -> int:
        return len(self.data)
    
class Labyrinth:
    def __init__(self, data: List[List[str]]) -> None:
        self.data = data
    
    def __getitem__(self, key: Tuple[int, int]) -> str:
        return self.data[key[0]][key[1]]
    
    def __setitem__(self, key: Tuple[int, int], other: str) -> None:
        self.data[key[0]][key[1]] = other
    
    def isPassable(self, x: int, y: int) -> bool:
        return self[x,y] in ("s", "o")

    def neighbors(self, x: int, y: int) -> Tuple[Tuple[int, int], ...]:
        out: List[Tuple[int, int]] = []
        for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
            if self.isPassable(x+i, y+j):
                out.append((x+i, y+j))
        return tuple(out)

class GridLabel(tk.Label):

    def __init__(self, x: int, y: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.bind("<Double-1>", self.findExit)
    
    def findExit(self, _: Any) -> None:
        p = Stack()
        if not lab.isPassable(self.x, self.y):
            return
        p.push((self.x, self.y))
        while len(p) > 0:
            x, y = p.pull()
            if lab[x,y] == "s":
                break
            lab[x,y] = "V"
            p.push(*lab.neighbors(x, y))
        update()



lab=Labyrinth([["1","1","1","1","1","1","1","1"],
                ["1","m","o","m","s","m","o","1"],
                ["1","o","o","o","o","o","o","1"],
                ["1","m","o","m","m","m","o","1"],
                ["1","o","m",'m',"o","o","o","1"],
                ["1","o","o","o","m","o","m","1"],
                ["1","m","o","m","o","o","m","1"],
                ["1","1","1","1","1","1","1","1"]])


main = tk.Tk()
main.title("Pathfinding")

def update():
    for i in gridText:
        for j in i:
            j["text"] = " " + lab[j.x, j.y] + " "

grid = []
gridText = []
for i in range(len(lab.data)):
    grid.append([])
    gridText.append([])
    for j in range(len(lab.data[0])):
        grid[i].append(tk.Frame(borderwidth=3, relief="groove", background="white"))
        grid[i][j].grid(row=i, column=j, sticky="news")
        gridText[i].append(GridLabel(i, j, master=grid[i][j], text="", background="white", font="TkFixedFont"))
        gridText[i][j].pack()

update()

main.mainloop()