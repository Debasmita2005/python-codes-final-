#This program check the triangle is valid or not
a = float(input("Enter first angle:"))
b = float(input("Enter second angle:"))
c = float(input("Enter third angle:"))

def triangle():
    total = a + b + c
    if total == 180:
        print("This triangle is valid")
    else:
        print("This triangle is not valid")

triangle()
