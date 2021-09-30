import math


class Rational:
    """Performs arithmetic with fractions"""

    def __init__(self, numerator=1, detonator=1):
        if not isinstance(numerator, int):
            raise ValueError("Wrong numerator!")
        if not isinstance(detonator, int):
            raise ValueError("Wrong detonator!")
        if not detonator:
            raise ZeroDivisionError("Division on zero!")
        self.__numerator = numerator
        self.__detonator = detonator

    def print_fraction(self):
        """Returns Rational numbers in the form a/b"""
        same_gdc = math.gcd(self.__numerator, self.__detonator)
        num = self.__numerator // same_gdc
        det = self.__detonator // same_gdc
        return '/'.join(list(map(str, (num, det))))

    def print_float(self):
        """Returns Rational numbers in floating-point format"""
        return self.__numerator / self.__detonator


if __name__ == "__main__":
    first = Rational(20, 15)
    print(first.print_fraction())
    print(first.print_float())
