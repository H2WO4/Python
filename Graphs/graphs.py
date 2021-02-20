from typing import Any, List, Tuple

class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.pathsTo: List[Tuple[Node, int]] = []
        self.pathsFrom: List[Tuple[Node, int]] = []
    
    def connect(self, other: Any, cost: int):
        self.pathsTo.append((other, cost))
        self.pathsFrom.append((other, cost))
    
    def link(self, other: Any, cost: int):
        self.pathsTo.append((other, cost))

class Graph:
    def __init__(self, *nodes: Node):
        self.nodes = [*nodes]


test = Graph(*[Node(i) for i in range(5)])

for i in test.nodes:
    print(i)