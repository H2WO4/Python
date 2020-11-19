from math import sqrt
from random import randint


"""
def Y(k):
    if k == 0:
        return A
    return 0.5*(Y(k-1) + (1/Z(k-1)))

def Z(k):
    if k == 0:
        return k
    return 0.5*(Z(k-1) + (1/Y(k-1)))
"""

class DimensionError(Exception):
    def __init__(self, message):
        self.message = message


class Matrix:
    def __init__(self, value):
        self.value = value
        self.lines = len(value)

        columnsArray = []
        for i in range(self.lines):
            columnsArray.append(len(value[i]))
        
        for i in range(1, self.lines):
            if columnsArray[i] != columnsArray[i-1]:
                raise DimensionError("Matrix is irregular hence cannot exist")
        
        self.columns = columnsArray[0]

        if self.lines == self.columns:
            self.__class__ = SquareMatrix
            self.__init__(self.value)

    def __str__(self):
        output = ""

        for i in range(len(self.value)):
            output += "[ "
            for j in self.value[i]:
                output += str(j) + " "
            output += "]\n"

        return output
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.lines == other.lines and self.columns == other.columns:
                output = []
                for i in range(self.lines):
                    output.append([])
                    for j in range(self.columns):
                        output[i].append(self.value[i][j] + other.value[i][j])
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            raise TypeError
    
    def __iadd__(self, other):
        return self+other
    
    def transpose(self):
        "Returns the transposed matrix"
        tempOutput = []
        for i in range(self.lines):
            for j in range(self.columns):
                tempOutput.append(self.value[i][j])
        output = []
        for i in range(self.columns):
            output.append([])
            for j in range(self.lines):
                output[i].append(tempOutput[i+(j*self.columns)])
        return Matrix(output)
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            output = []
            for i in range(self.lines):
                output.append([])
                for j in range(len(self.value[i])):
                    output[i].append(self.value[i][j] * other)
            return Matrix(output)
        else:
            return NotImplemented

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.lines:
                output = []
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
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        return self@other

    def __imatmul__(self, other):
        return self@other

    def __rimatmul__(self, other):
        return self@other
    
    def __truediv__(self, other):
        return self*(1/other)
    
    def __rtruediv__(self, other):
        return self*(1/other)

    def __idiv__(self, other):
        return self*(1/other)

    def __ridiv__(self, other):
        return self*(1/other)
    
    def hamadard(self, other):
        if isinstance(other, Matrix):
            if self.lines == other.lines and self.columns == other.columns:
                output = []
                for i in range(self.lines):
                    output.append([])
                    for j in range(len(self.value[i])):
                        output[i].append(self.value[i][j] * other.value[i][j])
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            return NotImplemented
    
    def kronecker(self, other):
        if isinstance(other, Matrix):
            output = []
            tempOutput = []
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

        else:
            return NotImplemented

    def __neg__(self):
        return self*(-1)

    def augment(self, other):
        if isinstance(other, Matrix):
            if self.lines == other.lines:
                output = self.value
                for i in range(other.lines):
                    for j in range(other.columns):
                        output[i].append(other.value[i][j])
                return Matrix(output)
            else:
                raise DimensionError("Different numbers of lines and columns in operands matrices")
        else:
            return NotImplemented

class SquareMatrix(Matrix):
    def __init__(self, value):
        self.value = value
        self.lines = len(value)
        columnsArray = []
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
    
    def invert(self):
        if self.lines == 2:
            output = self
            output.value[0][1] = -output.value[0][1]
            output.value[1][0] = -output.value[1][0]
            output *= 1/self.determinant
            return Matrix(output.value)
        if self.lines == 3:
            cofactor = []
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
            cofactor = Matrix(cofactor)
            return Matrix((cofactor * (1/self.determinant)).value)
    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self*(1/other)
        
        if isinstance(other, SquareMatrix):
            if self.lines == other.lines:
                return self*(other.invert())

    def __rtruediv__(self, other):
        return self/other
    
    def __idiv__(self, other):
        return self/other

    def __ridiv__(self, other):
        return self/other
        

def identityMatrix(dimension):
    "Create an identity matrix based on the dimension given"
    output = []
    for i in range(dimension):
        output.append([])
        for j in range(dimension):
            if i == j:
                output[i].append(1)
            else:
                output[i].append(0)
    return Matrix(output)

"""
def randomMatrix(lines, columns, min, max):
    output = []
    for i in range(lines):
        output.append([])
        for j in range(columns):
            output[i].append(randint(min, max))
    return Matrix(output)
"""

A = Matrix([[2,3],[5,7]])
B = Matrix([[6,2],[4,0]])

print(A@B)
print(A.hamadard(B))