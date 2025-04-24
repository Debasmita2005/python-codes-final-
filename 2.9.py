#This program print absolute value of given number
a = float(input("Enter a number:"))

def absolute():
    if a >= 0:
        print("Absolute value of", a, "is", a)
    else:
        print("Absolute value of", a, "is", a*-1)

absolute()
