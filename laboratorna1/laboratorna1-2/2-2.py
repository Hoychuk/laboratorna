from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        if not isinstance(numerator, int):
            raise TypeError("Wrong data")
        if not isinstance(denominator, int):
            raise TypeError("Wrong data")
        self.numerator = numerator
        self.denominator = denominator

    def float_form(self):
        return self.numerator / self.denominator

    def ab_form(self):
        return f'{self.numerator//gcd(self.numerator,self.denominator)} / {self.denominator//gcd(self.numerator,self.denominator)}'

x = Rational(5, 6)
y = Rational(10, 7)
print(x.float_form())
print(y.ab_form())