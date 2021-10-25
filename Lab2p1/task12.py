import math


class Rational:
    """
    Class with numerator and predator
    Performs arithmetic with fractions
    """

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
        same_gcd = math.gcd(self.__numerator, self.__detonator)
        num = self.__numerator // same_gcd
        det = self.__detonator // same_gcd
        return f"{num} / {det}"

    def print_float(self):
        """Returns Rational numbers in floating-point format"""
        return self.__numerator / self.__detonator

    def __str__(self):
        return f"numerator - {self.__numerator}, width - {self.__detonator}\n" \
               f"Area: {self.print_fraction()}, perimeter - {self.print_float()}\n"


if __name__ == "__main__":
    first = Rational(20, 15)
    print(first.print_fraction())
    print(first.print_float())
