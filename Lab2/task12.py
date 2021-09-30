import math

class Rational:
    def __init__(self, numerator=1, detonator=1):
        if not isinstance(numerator, int):
            raise ValueError("Wrong numerator!")
        if not isinstance(detonator, int):
            raise ValueError("Wrong detonator!")
        if not detonator:
            raise ZeroDivisionError("Division on zero!")

    def print_fraction(self):
        math.gcd(numerator, detonator)

    def print_float(self):
        return self.__numerator / self.__detonator


if __name__ == "__main__":
    first = Rational()
    first.set_num(5)
    first.set_det(0)
    first.print_float()