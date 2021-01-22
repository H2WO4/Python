from typing import Tuple, Union
from Maths.Complex import Complex

def solve_second(a: float, b: float, c: float) -> Union[float, Tuple[Complex, Complex]]:
    if a == 0:
        return -c/b
    discr = Complex(b ** 2 - 4 * a * c, 0)
    print(discr, discr.root(2))
    return (b - discr.root(2))/(2 * a), (b + discr.root(2))/(2 * a)


a = solve_second(2, 9, -5)
if isinstance(a, tuple):
    print(*a)
else:
    print(a)