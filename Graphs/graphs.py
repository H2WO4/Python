from typing import Any, List, Tuple

class Node:
    def __init__(self, value: int):
        self.value: int = value
    
    def __str__(self) -> str:
        return str(self.value)

class Graph:
    def __init__(self, size: int):
        self.nodes: List[Node] = []
        for i in range(size):
            self.nodes.append(Node(i))

        self.relations: List[Tuple[Node, Node]] = []    
    
    def connect(self, other1: Node, other2: Node) -> None:
        if other1 == other2:
            return
        
        if (other1, other2) not in self.relations:
            self.relations.append((other1, other2))
        if (other2, other1) not in self.relations:
            self.relations.append((other2, other1))
    
    def is_linked(self, other1, other2) -> bool:
        return (other1, other2) in self.relations


test = Graph(5)

for i in range(5):
    for j in range(3):
        test.connect(test.nodes[i], test.nodes[j])

test.relations.sort(key=lambda a: a[0].value)

for i in test.relations:
    print("({}, {})".format(i[0], i[1]))