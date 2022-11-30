from math import gcd


class Rational:

    def __init__(self, nominator, denominator):
        if not isinstance(nominator, int):
            raise TypeError("Wrong data. Numerator")
        elif not isinstance(denominator, int):
            raise TypeError("Wrong data. Denominator")
        elif denominator == 0:
            raise ZeroDivisionError
        self.nominator = nominator
        self.denominator = denominator

    def float_form(self):
        return self.nominator / self.denominator

    def ab_form(self):
        return f'{self.nominator // gcd(self.nominator, self.denominator)} / {self.denominator // gcd(self.nominator, self.denominator)}'

    def find_lcd(self, num1, num2):
        lcd = max(num1, num2)
        while not (lcd % num1 == 0 and lcd % num2 == 0):
            lcd += 1
        return lcd

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Error: Other must be Rational type")
        else:
            lcd = self.find_lcd(self.denominator, other.denominator)
            nominator1 = int(self.nominator * lcd / self.denominator)
            nominator2 = int(other.nominator * lcd / other.denominator)
            return Rational(nominator1 + nominator2, lcd)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise Exception("other must be of type Rational")
        else:
            lcd = self.find_lcd(self.denominator, other.denominator)
            nominator1 = int(self.nominator * lcd / self.denominator)
            nominator2 = int(other.nominator * lcd / other.denominator)
            return Rational(nominator1 - nominator2, lcd)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Error: Other must be Rational type")
        else:
            return Rational(self.nominator * other.nominator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Error: Other must be Rational type")
        else:
            return Rational(self.nominator * other.denominator, self.denominator * other.nominator)

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Error: Other must be Rational type")
        else:
            return self.nominator == other.nominator and self.denominator == other.denominator


fraction = Rational(2, 3)
fraction1 = Rational(3, 4)
print(fraction.ab_form())
print(fraction1.ab_form())
test = fraction + fraction1
print(test.float_form())
test = fraction - fraction1
print(test.float_form())
test = fraction * fraction1
print(test.float_form())
test = fraction / fraction1
print(test.float_form())
