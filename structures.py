from typing import Any, List, Tuple


class ObjectList:
    def __init__(self, data: List[Any] = []) -> None:
        self.data = data

    def __len__(self) -> int:
        return len(self.data)
    
    def __str__(self) -> str:
        return str(self.data)


class Stack(ObjectList):
    def push(self, *values: Any) -> None:
        self.data = list(values) + self.data
    
    def pull(self, amount: int=1) -> Tuple[Any, ...]:
        out = self.data[:amount]
        self.data = self.data[amount:]
        return tuple(out)
    
    def peek(self, amount: int=1) -> Tuple[Any, ...]:
        return tuple(self.data[:amount])
    
    def clear(self) -> None:
        self.data = []


class Queue(ObjectList):
    def push(self, *values: Any) -> None:
        self.data = self.data + list(values)
    
    def pull(self, amount: int=1) -> Tuple[Any, ...]:
        out = self.data[:amount]
        self.data = self.data[amount:]
        return tuple(out)
    
    def peek(self, amount: int=1) -> Tuple[Any, ...]:
        return tuple(self.data[:amount])
    
    def clear(self) -> None:
        self.data = []


p = Stack()