# Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.

class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date


d1 = Date(24, 4, 2025)
d2 = Date(24, 4, 2025)
print("Dates are equal" if d1 == d2 else "Dates are not equal")
