from fractions import Fraction as PythonFraction


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.fraction = PythonFraction(numerator, denominator)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type for +: 'Fraction' and '{}'".format(type(other).__name__))
        return Fraction(self.fraction + other.fraction)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for -: 'Fraction' and '{}'".format(type(other).__name__))
        return Fraction(self.fraction - other.fraction)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for *: 'Fraction' and '{}'".format(type(other).__name__))
        return Fraction(self.fraction * other.fraction)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for /: 'Fraction' and '{}'".format(type(other).__name__))
        if other.fraction == 0:
            raise ValueError("Division by zero.")
        return Fraction(self.fraction / other.fraction)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.fraction == other.fraction

    def __str__(self):
        return str(self.fraction)


x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)
