from math import sqrt
from typing import List
from __future__ import annotations


class DimensionError(Exception):
    def __init__(self, message: str):
        self.message = message


class Matrix:
    def __init__(self, value: List[List[float]]) -> None:
        self.value = value
        self.lines = len(value)

        columnsArray: List[int] = []
        for i in range(self.lines):
            columnsArray.append(len(value[i]))
        
        for i in range(1, self.lines):
            if columnsArray[i] != columnsArray[i-1]:
                raise DimensionError("Matrix is irregular hence cannot exist")
        
        self.columns = columnsArray[0]

        if self.lines == self.columns:
            self.__class__ = SquareMatrix
            self.__init__(self.value)

    def __str__(self) -> str:
        output = ""
        for i in range(len(self.value)):
            output += "[ "
            for j in self.value[i]:
                output += str(j) + " "
            output += "]\n"

        return output
    
    def __add__(self, other: Matrix) -> Matrix:
        if self.lines == other.lines and self.columns == other.columns:
            output: List[list[float]] = []
            for i in range(self.lines):
                output.append([])
                for j in range(self.columns):
                    output[i].append(self.value[i][j] + other.value[i][j])
            return Matrix(output)
        else:
            raise DimensionError("Different numbers of lines and columns in operands matrices")
    
    def __iadd__(self, other: Matrix) -> Matrix: return self+other
    
    def transpose(self) -> Matrix:
        "Returns the transposed matrix"
        tempOutput: List[float] = []
        for i in range(self.lines):
            for j in range(self.columns):
                tempOutput.append(self.value[i][j])
        output: List[List[float]] = []
        for i in range(self.columns):
            output.append([])
            for j in range(self.lines):
                output[i].append(tempOutput[i+(j*self.columns)])
        return Matrix(output)
    
    def __mul__(self, other: float) -> Matrix:
        output: List[List[float]] = []
        for i in range(self.lines):
            output.append([])
            for j in range(len(self.value[i])):
                output[i].append(self.value[i][j] * other)
        return Matrix(output)

    def __matmul__(self, other: Matrix) -> Matrix:
        if self.columns == other.lines:
            output: List[List[float]] = []
            for i in range(self.lines):
                output.append([])
                for j in range(other.columns):
                    futureOutput = 0
                    for k in range(self.columns):
                        futureOutput += self.value[i][k] * other.value[k][j]
                    output[i].append(futureOutput)
            return Matrix(output)
        else:
            raise DimensionError("Different numbers of lines and columns in operands matrices")

    def __rmatmul__(self, other: Matrix) -> Matrix: return self @ other

    def __imatmul__(self, other: Matrix) -> Matrix: return self @ other

    def __rimatmul__(self, other: Matrix) -> Matrix: return self @ other
    
    def __truediv__(self, other: float) -> Matrix: return self*(1/other)
    
    def __rtruediv__(self, other: float) -> Matrix: return self*(1/other)

    def __idiv__(self, other: float) -> Matrix: return self*(1/other)

    def __ridiv__(self, other: float) -> Matrix: return self*(1/other)
    
    def hamadard(self, other: Matrix) -> Matrix:
        if self.lines == other.lines and self.columns == other.columns:
            output: List[List[float]] = []
            for i in range(self.lines):
                output.append([])
                for j in range(len(self.value[i])):
                    output[i].append(self.value[i][j] * other.value[i][j])
            return Matrix(output)
        else:
            raise DimensionError("Different numbers of lines and columns in operands matrices")
    
    def kronecker(self, other: Matrix) -> Matrix:
        output: List[List[float]] = []
        tempOutput: List[float] = []
        for i in range(self.lines * other.lines):
            output.append([])
        for i in range(self.lines):
            for j in range(self.columns):
                for k in range(other.lines):
                    for l in range(other.columns):
                        tempOutput.append(self.value[i][j] * other.value[k][l])
        for i in range(len(tempOutput)):
            if i % sqrt(len(tempOutput)) >= sqrt(len(tempOutput)) // 2:
                output[i // len(tempOutput) + 1 + self.lines // 2].append(tempOutput[i])
            else:
                output[i // len(tempOutput) + self.lines // 2].append(tempOutput[i])
        return Matrix(output)

    def __neg__(self) -> Matrix: return self * -1

    def augment(self, other: Matrix) -> Matrix:
        if self.lines == other.lines:
            output = self.value
            for i in range(other.lines):
                for j in range(other.columns):
                    output[i].append(other.value[i][j])
            return Matrix(output)
        else:
            raise DimensionError("Different numbers of lines and columns in operands matrices")

class SquareMatrix(Matrix):
    def __init__(self, value: List[List[float]]):
        self.value = value
        self.lines = len(value)
        columnsArray: List[float] = []
        for i in range(self.lines):
            columnsArray.append(len(value[i]))
        for i in range(1, self.lines):
            if columnsArray[i] != columnsArray[i-1]:
                raise DimensionError("Matrix is irregular hence cannot exist")
        self.columns = columnsArray[0]

        if self.lines != self.columns:
            raise DimensionError("Square matrix has different number of lines and columns")
        
        det1, det2 = self.value[0][0], self.value[self.lines-1][0]
        for i in range(self.lines):
            if i != 0:
                det1 *= self.value[i][i]
                det2 *= self.value[self.lines-i-1][i]
        self.determinant = det1 - det2

        output = 0
        for i in range (self.lines):
            output += self.value[i][i]
        self.trace = output
    
    def invert(self) -> SquareMatrix:
        if self.lines == 2:
            output = self
            output.value[0][1] = -output.value[0][1]
            output.value[1][0] = -output.value[1][0]
            output *= 1/self.determinant
            return SquareMatrix(output.value)

        else:
            cofactor: List[List[float]] = []
            for i in range(3):
                cofactor.append([])
                for _ in range(3):
                    cofactor[i].append(0)
            cofactor[0][0] = self.value[1][1] * self.value[2][2] - self.value[1][2] * self.value[2][1]
            cofactor[0][1] = -(self.value[0][1] * self.value[2][2] - self.value[0][2] * self.value[2][1])
            cofactor[0][2] = self.value[0][1] * self.value[1][2] - self.value[0][2] * self.value[1][1]
            cofactor[1][0] = -(self.value[1][0] * self.value[2][2] - self.value[1][2] * self.value[2][0])
            cofactor[1][1] = self.value[0][0] * self.value[2][2] - self.value[0][2] * self.value[2][0]
            cofactor[1][2] = -(self.value[0][0] * self.value[2][1] - self.value[0][1] * self.value[2][0])
            cofactor[2][0] = self.value[1][0] * self.value[2][1] - self.value[1][1] * self.value[2][0]
            cofactor[2][1] = -(self.value[0][0] * self.value[1][2] - self.value[0][2] * self.value[1][0])
            cofactor[2][2] = self.value[0][0] * self.value[1][1] - self.value[0][1] * self.value[1][0]
            return SquareMatrix((Matrix(cofactor) * (1/self.determinant)).value)
    
    def __truediv__(self, other: float | SquareMatrix) -> SquareMatrix:
        if isinstance(other, SquareMatrix):
            if self.lines == other.lines:
                return self*(other.invert()) # type: ignore
            else:
                raise DimensionError("")
        
        return self*(1/other) # type: ignore

    def __rtruediv__(self, other: float | SquareMatrix) -> SquareMatrix: return self/other
    
    def __idiv__(self, other: float | SquareMatrix) -> SquareMatrix: return self/other

    def __ridiv__(self, other: float | SquareMatrix) -> SquareMatrix: return self/other
        

def identityMatrix(dimension: int) -> SquareMatrix:
    "Create an identity matrix based on the dimension given"
    output: List[List[float]] = []
    for i in range(dimension):
        output.append([])
        for j in range(dimension):
            if i == j:
                output[i].append(1)
            else:
                output[i].append(0)
    return SquareMatrix(output)


A = Matrix([[2,3],[5,7]])
B = Matrix([[6,2],[4,0]])

print(A @ B)
print(A.hamadard(B))