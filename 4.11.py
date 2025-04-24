#This program calculate sin(x)
a = float(input("Enter the angle in degrees:"))
x = a * 3.14159 / 180

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def sin():
    sin = 0
    j = 0
    for i in range(1, 8, 2):
        sin += ((((-1) ** j) * x ** i) / factorial(i))
        j += 1
    print(f"Value of sin({a}) is {sin}")

sin()
