from typing import Generic, List, TypeVar


T = TypeVar("T")

class Array(Generic[T]):
    def __init__(self, content: List[List[T]]) -> None:
        self.content = content
    
    def __getitem__(self, index: slice) -> T | List[T] | List[List[T]]:
        match index.start, index.stop:
            case None, None:
                return self.content
            case x, None:
                return self.content[x]
            case None, x:
                return [i[x] for i in self.content]
            case x, y:
                return self.content[x][y]
            case _:
                raise ValueError

A = Array([[2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]])
B = Array([["a", "b"], [2, "d"]])


print(A[0:])
print(B[:1])