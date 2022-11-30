class Calendar:
    def max_days(self, month, year):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month == 2:
            if year % 4 == 0:
                return 29
            return 28
        return 30

    def __init__(self, day, month, year):
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if 0 < day <= self.max_days(month, year):
                self.day = day
            else:
                raise Exception("Error: Day must be greater than 0 and less than " + str(self.max_days(month, year)))
            if 0 < month < 13:
                self.month = month
            else:
                raise Exception("Error: Month must be greater than 0 and less than 13")
            if year > 0:
                self.year = year
            else:
                raise Exception("Error: Year must be greater than 0")
        else:
            raise Exception("Date must be of type int")

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __iadd__(self, other):
        if isinstance(other, Calendar):
            max_days = self.max_days(self.month, self.year)
            self.day += other.day
            self.month += other.month
            self.year += other.year

            while self.day > max_days:
                self.day -= max_days
                self.month += 1

            while self.month > 12:
                self.month -= 12
                self.year += 1

            return self
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __isub__(self, other):
        if isinstance(other, Calendar):
            max_days = self.max_days(self.month, self.year)
            self.day -= other.day
            self.month -= other.month
            self.year -= other.year

            while self.day <= 0:
                self.day += max_days
                self.month -= 1

            while self.month <= 0:
                self.month += 12
                self.year -= 1

            return self
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __eq__(self, other):
        if isinstance(other, Calendar):
            return self.day == other.day and self.month == other.month and self.year == other.year
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __ne__(self, other):
        if isinstance(other, Calendar):
            return self.day != other.day or self.month != other.month or self.year != other.year
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __gt__(self, other):
        if isinstance(other, Calendar):
            if self.year != other.year:
                return self.year > other.year
            elif self.month != other.month:
                return self.month > other.month
            else:
                return self.day > other.day
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __lt__(self, other):
        if isinstance(other, Calendar):
            if self.year != other.year:
                return self.year < other.year
            elif self.month != other.month:
                return self.month < other.month
            else:
                return self.day < other.day
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __ge__(self, other):
        if isinstance(other, Calendar):
            if self.year != other.year:
                return self.year >= other.year
            elif self.month != other.month:
                return self.month >= other.month
            else:
                return self.day >= other.day
        else:
            raise Exception("Error: Other date must be an instance of Calendar")

    def __le__(self, other):
        if isinstance(other, Calendar):
            if self.year != other.year:
                return self.year <= other.year
            elif self.month != other.month:
                return self.month <= other.month
            else:
                return self.day <= other.day
        else:
            raise Exception("Error: Other date must be an instance of Calendar")


myCalendar1 = Calendar(30, 11, 2022)
print(myCalendar1)
myCalendar1 += Calendar(12, 3, 3)
print(myCalendar1)
myCalendar1 -= Calendar(21, 8, 5)
print(myCalendar1)
print(myCalendar1 >= Calendar(10, 10, 1010))
print(myCalendar1 < Calendar(10, 10, 1010))