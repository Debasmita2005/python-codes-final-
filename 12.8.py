# 8.	Implement a String class containing the following functions:
# a.	Overloaded += operator function to perform string concatenation
# b.	Method toLower() to convert upper case letters to lower case.
# c.	Method toUpper() to convert lower case letters to upper case


class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def toLower(self):
        return self.value.lower()

    def toUpper(self):
        return self.value.upper()


s = String("Hello")
s += " World"
print(s.value)         
print(s.toLower())     
print(s.toUpper())     

