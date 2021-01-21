from math import atan, cos, sin, pi, sqrt, e, log
from typing import Any, Union


def ComplexArg(modulus: float, argument: float) -> Any:
    natural = round(modulus*cos(argument), 12)
    imaginary = round(modulus*sin(argument), 12)
    if int(natural) == natural:
        natural = int(natural)
    if int(imaginary) == imaginary:
        imaginary = int(imaginary)
    return Complex(natural, imaginary)

class Complex:
    def __init__(self, natural: float, imaginary: float) -> None:
        self.natural = natural
        self.imaginary = imaginary
        self.modulus = sqrt(natural**2+imaginary**2)
        if natural != 0 or imaginary > 0:
            self.argument = 2*atan(imaginary/(self.modulus+natural))
        elif imaginary < 0:
            self.argument = pi
    
    def __str__(self) -> str:
        if self.imaginary > 0 and self.natural:
            return "{}+{}i".format(self.natural, self.imaginary)
        elif self.imaginary < 0 and self.natural:
            return "{}{}i".format(self.natural, self.imaginary)
        elif self.imaginary and not self.natural:
            return "{}i".format(self.imaginary)
        else:
            return "{}".format(self.natural)

    def __add__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, Complex):
            return Complex(self.natural+other.natural, self.imaginary+other.imaginary)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.natural+other, self.imaginary)
        else:
            return NotImplemented
    
    def __radd__(self, other: float) -> Any:
        return self+other

    def __iadd__(self, other: Union[float, Any]) -> Any:
        return self+other

    def __riadd__(self, other: float) -> Any:
        return self+other

    def __neg__(self) -> Any:
        return Complex(-self.natural, -self.imaginary)

    def __sub__(self, other: Union[float, Any]) -> Any:
        return self+(-other)
    
    def __rsub__(self, other: float) -> Any:
        return self+(-other)

    def __isub__(self, other: Union[float, Any]) -> Any:
        return self+(-other)

    def __risub__(self, other: float) -> Any:
        return self+(-other)
    
    def __mul__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, Complex):
            return Complex(self.natural*other.natural-self.imaginary*other.imaginary, self.natural*other.imaginary+self.imaginary*other.natural)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.natural*other, self.imaginary*other)
        else:
            return NotImplemented
    
    def __rmul__(self, other: float) -> Any:
        return self*other
    
    def __imul__(self, other: Union[float, Any]) -> Any:
        return self*other

    def __rimul__(self, other: float) -> Any:
        return self*other

    def invert(self) -> Any:
        return Complex(self.natural/(self.natural**2+self.imaginary**2), -self.imaginary/(self.natural**2+self.imaginary**2))
    
    def __truediv__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, Complex):
            return self*other.invert()
        elif isinstance(other, int) or isinstance(other, float):
            return self*(1/other)
    
    def __rtruediv__(self, other: float) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Complex(other, 0)/self
    
    def __idiv__(self, other: Union[float, Any]) -> Any:
        return self/other

    def __ridiv__(self, other: float) -> Any:
        return self/other
    
    def __pow__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return ComplexArg(self.modulus**other, self.argument*other)
        elif isinstance(other, Complex):
            return (self.modulus**other.natural*e**(-other.imaginary*self.argument))*Complex(cos(other.imaginary*log(self.modulus)+other.natural*self.argument), sin(other.imaginary*log(self.modulus)+other.natural*self.argument))
        else:
            return NotImplemented
        
    def __rpow__(self, other: float) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Complex(other, 0)**self
        else:
            return NotImplemented

    def __ipow__(self, other: Union[float, Any]) -> Any:
        return self**other

    def __ripow__(self, other: float) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Complex(other, 0)**self
        else:
            return NotImplemented

    def root(self, other: float) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return self**(1/other)
    
    def log(self, other: float) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Complex(log(self.modulus, other), self.argument)
    
    def conjugate(self) -> Any:
        return Complex(self.natural, -self.imaginary)

    def exponential(self) -> str:
        if self.modulus == 0:
            return "0"
        elif self.modulus == 1:
            return "e**({}i)".format(self.argument)
        elif self.modulus == -1:
            return "-e**({}i)".format(self.argument)
        else:
            return "{}e**({}i)".format(self.modulus, self.argument)

a = Complex(2, 3)
b = Complex(3, 2)
i = Complex(0, 1)