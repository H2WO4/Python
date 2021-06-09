from typing import Any, Generic, List, Tuple, TypeVar

T = TypeVar("T")

class ObjectList(Generic[T]):
    def __init__(self, data: List[T] = []) -> None:
        self.data = data

    def __len__(self) -> int:
        return len(self.data)


class Stack(ObjectList[T]):
    def push(self, *values: T) -> None:
        self.data: List[T] = list(values) + self.data
    
    def pull(self, amount: int=1) -> Tuple[Any, ...]:
        out = self.data[:amount]
        self.data = self.data[amount:]
        return tuple(out)
    
    def peek(self, amount: int=1) -> Tuple[Any, ...]:
        return tuple(self.data[:amount])
    
    def clear(self) -> None:
        self.data = []
    
    def __str__(self) -> str:
        return "|".join([str(i) for i in reversed(self.data)]) + " <->"


class Queue(ObjectList[T]):
    def push(self, *values: Any) -> None:
        self.data: List[T] = self.data + list(reversed(values))
    
    def pull(self, amount: int=1) -> Tuple[Any, ...]:
        out = self.data[-amount:]
        self.data = self.data[:-amount]
        return tuple(out)
    
    def peek(self, amount: int=1) -> Tuple[Any, ...]:
        return tuple(self.data[:amount])
    
    def clear(self) -> None:
        self.data = []
    
    def __str__(self) -> str:
        return "-> " + "|".join([str(i) for i in self.data]) + " ->"


p = Stack[int]()
p.push(*range(10))
print(p)
print(*p.pull(3))