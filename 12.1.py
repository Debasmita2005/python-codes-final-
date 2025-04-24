# Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition, subtraction, multiplication and division.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print(f"{self.real} + {self.imag}i")

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __multiply__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __div__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

c1 = Complex(5, 4)
c2 = Complex(4, 3)
c3 = c1 + c2
c4 = c1 - c2
c5 = c1*c2
c6 = c1/c2

c3.display()
c4.display()
c5.display()
c6.display()

