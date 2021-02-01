from math import atan2, cos, sin, sqrt, e, log
from typing import Any, Union


def ComplexArg(mod: float, arg: float) -> Any:
    nat = round(mod*cos(arg), 12)
    imag = round(mod*sin(arg), 12)
    if int(nat) == nat:
        nat = int(nat)
    if int(imag) == imag:
        imag = int(imag)
    return Complex(nat, imag)

class Complex:
    def __init__(self, nat: float, imag: float) -> None:
        self.nat = nat
        self.imag = imag
        self.mod = sqrt(nat**2+imag**2)
        self.arg = atan2(imag, nat)
    
    def __str__(self) -> str:
        if self.imag > 0 and self.nat:
            return "{}+{}i".format(self.nat, self.imag)
        elif self.imag < 0 and self.nat:
            return "{}{}i".format(self.nat, self.imag)
        elif self.imag and not self.nat:
            return "{}i".format(self.imag)
        else:
            return "{}".format(self.nat)

    def __add__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, Complex):
            return Complex(self.nat+other.nat, self.imag+other.imag)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.nat+other, self.imag)
        else:
            return NotImplemented
    
    def __radd__(self, other: float) -> Any:
        return self+other

    def __iadd__(self, other: Union[float, Any]) -> Any:
        return self+other

    def __riadd__(self, other: float) -> Any:
        return self+other

    def __neg__(self) -> Any:
        return Complex(-self.nat, -self.imag)

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
            return Complex(self.nat*other.nat-self.imag*other.imag, self.nat*other.imag+self.imag*other.nat)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.nat*other, self.imag*other)
        else:
            return NotImplemented
    
    def __rmul__(self, other: float) -> Any:
        return self*other
    
    def __imul__(self, other: Union[float, Any]) -> Any:
        return self*other

    def __rimul__(self, other: float) -> Any:
        return self*other

    def invert(self) -> Any:
        return Complex(self.nat/(self.nat**2+self.imag**2), -self.imag/(self.nat**2+self.imag**2))
    
    def __truediv__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, Complex):
            return self*other.invert()
        elif isinstance(other, int) or isinstance(other, float):
            return self*(1/other)
    
    def __rdiv__(self, other: float) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return Complex(other, 0)/self
    
    def __idiv__(self, other: Union[float, Any]) -> Any:
        return self/other

    def __ridiv__(self, other: float) -> Any:
        return self/other
    
    def __pow__(self, other: Union[float, Any]) -> Any:
        if isinstance(other, int) or isinstance(other, float):
            return ComplexArg(self.mod**other, self.arg*other)
        elif isinstance(other, Complex):
            return (self.mod**other.nat*e**(-other.imag*self.arg))*Complex(cos(other.imag*log(self.mod)+other.nat*self.arg), sin(other.imag*log(self.mod)+other.nat*self.arg))
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
            return Complex(log(self.mod, other), self.arg)
    
    def conjugate(self) -> Any:
        return Complex(self.nat, -self.imag)

    def exponential(self) -> str:
        if self.mod == 0:
            return "0"
        elif self.mod == 1:
            return "e**({}i)".format(self.arg)
        elif self.mod == -1:
            return "-e**({}i)".format(self.arg)
        else:
            return "{}e**({}i)".format(self.mod, self.arg)

