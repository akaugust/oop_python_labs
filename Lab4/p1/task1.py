import math


class Rational:
    """
    Class with numerator and predator
    Performs arithmetic with fractions and integers
    """

    def __init__(self, numerator=1, denominator=1):
        self.numerator, self.denominator = Rational.same_gdc(numerator, denominator)

    @property
    def numerator(self):
        """numerator getter"""
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        """numerator setter"""
        if not isinstance(numerator, int):
            raise ValueError("Wrong numerator!")
        self.__numerator = numerator

    @property
    def denominator(self):
        """denominator getter"""
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        """denominator setter"""
        if not isinstance(denominator, int):
            raise ValueError("Wrong denominator!")
        if not denominator:
            raise ZeroDivisionError("Division on zero!")
        self.__denominator = denominator

    def __add__(self, other):
        """ + overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        elif isinstance(other, int):
            num = self.numerator + self.denominator * other
            return Rational(num, self.denominator)
        else:
            return NotImplemented

    def __iadd__(self, other):
        """ += overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            den = self.denominator * other.denominator
            self.numerator, self.denominator = Rational.same_gdc(num, den)
            return self
        elif isinstance(other, int):
            num = self.numerator + self.denominator * other
            self.numerator, self.denominator = Rational.same_gdc(num, self.denominator)
            return self
        else:
            return NotImplemented

    def __sub__(self, other):
        """ - overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        elif isinstance(other, int):
            num = self.numerator - self.denominator * other
            return Rational(num, self.denominator)
        else:
            return NotImplemented

    def __isub__(self, other):
        """ -= overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            den = self.denominator * other.denominator
            self.numerator, self.denominator = Rational.same_gdc(num, den)
            return self
        elif isinstance(other, int):
            num = self.numerator - self.denominator * other
            self.numerator, self.denominator = Rational.same_gdc(num, self.denominator)
            return self
        else:
            return NotImplemented

    def __mul__(self, other):
        """ * overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Rational(num, den)
        elif isinstance(other, int):
            num = self.numerator * other
            return Rational(num, self.denominator)
        else:
            return NotImplemented

    def __imul__(self, other):
        """ *= overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            self.numerator, self.denominator = Rational.same_gdc(num, den)
            return self
        elif isinstance(other, int):
            num = self.numerator * other
            self.numerator, self.denominator = Rational.same_gdc(num, self.denominator)
            return self
        else:
            return NotImplemented

    def __truediv__(self, other):
        """ / overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return Rational(num, den)
        elif isinstance(other, int):
            num = self.denominator * other
            return Rational(self.numerator, num)
        else:
            return NotImplemented

    def __idiv__(self, other):
        """ /= overload"""
        if isinstance(other, Rational):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            self.numerator, self.denominator = Rational.same_gdc(num, den)
            return self
        elif isinstance(other, int):
            den = self.denominator * other
            self.numerator, self.denominator = Rational.same_gdc(self.numerator, den)
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """ == overload"""
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            return NotImplemented

    def __ne__(self, other):
        """ != overload"""
        if isinstance(other, Rational):
            return self.numerator != other.numerator or self.denominator != other.denominator
        elif isinstance(other, int):
            return self.numerator != other * self.denominator
        else:
            return NotImplemented

    def __lt__(self, other):
        """ < overload"""
        if isinstance(other, Rational):
            return self.numerator * other.denominator < self.denominator * other.numerator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            return NotImplemented

    def __le__(self, other):
        """ <= overload"""
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= self.denominator * other.numerator
        elif isinstance(other, int):
            return self.numerator <= other * self.denominator
        else:
            return NotImplemented

    def __gt__(self, other):
        """ > overload"""
        if isinstance(other, Rational):
            return self.numerator * other.denominator > self.denominator * other.numerator
        elif isinstance(other, int):
            return self.numerator > other * self.denominator
        else:
            return NotImplemented

    def __ge__(self, other):
        """ >= overload"""
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= self.denominator * other.numerator
        elif isinstance(other, int):
            return self.numerator >= other * self.denominator
        else:
            return NotImplemented

    @staticmethod
    def same_gdc(numerator, denominator):
        needed_gcd = math.gcd(numerator, denominator)
        num = numerator // needed_gcd
        den = denominator // needed_gcd
        return num, den

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    a = Rational(12, 10)
    b = Rational(3, 10)
    c = 2
    print(a, b, sep='\n')

    sum_rational = a + b
    sum_int = a + c
    print(f'{a} + {b} = {sum_rational}')
    print(f'{a} + {c} = {sum_int}')

    sub_rational = a - b
    sub_int = a - c
    print(f'{a} - {b} = {sub_rational}')
    print(f'{a} - {c} = {sub_int}')

    mul_rational = a * b
    mul_int = a * c
    print(f'{a} * {b} = {mul_rational}')
    print(f'{a} * {c} = {mul_int}')

    truediv_rational = a / b
    truediv_int = a / c
    print(f'{a} * {b} = {truediv_rational}')
    print(f'{a} * {c} = {truediv_int}\n')

    d = Rational(2, 3)
    d += a
    print(f'2/3 += {a} -> {d}')
    d += c
    print(f' += {c} -> {d}')
    d -= b
    print(f' -= {b} -> {d}')
    d -= c
    print(f' -= {c} -> {d}')
    d *= b
    print(f' *= {b} -> {d}')
    d *= c
    print(f' *= {c} -> {d}')
    d /= a
    print(f' /= {a} -> {d}')
    d /= c
    print(f' /= {c} -> {d}\n')




    if a == b:
        print(f'{a} == {b} is true')
    else:
        print(f'{a} == {b} is false')
    if a == c:
        print(f'{a} == {c} is true')
    else:
        print(f'{a} == {c} is false')

    if a != b:
        print(f'{a} != {b} is true')
    else:
        print(f'{a} != {b} is false')
    if a != c:
        print(f'{a} != {c} is true')
    else:
        print(f'{a} != {c} is false')

    if a < b:
        print(f'{a} < {b} is true')
    else:
        print(f'{a} < {b} is false')
    if a < c:
        print(f'{a} < {c} is true')
    else:
        print(f'{a} < {c} is false')

    if a <= b:
        print(f'{a} <= {b} is true')
    else:
        print(f'{a} <= {b} is false')
    if a <= c:
        print(f'{a} <= {c} is true')
    else:
        print(f'{a} <= {c} is false')

    if a > b:
        print(f'{a} > {b} is true')
    else:
        print(f'{a} > {b} is false')
    if a > c:
        print(f'{a} > {c} is true')
    else:
        print(f'{a} > {c} is false')

    if a >= b:
        print(f'{a} >= {b} is true')
    else:
        print(f'{a} >= {b} is false')
    if a >= c:
        print(f'{a} >= {c} is true')
    else:
        print(f'{a} >= {c} is false')
