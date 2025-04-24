#This program calculate area & perimeter of a rectangle 
L = float(input("Enter the length of a rectangle:"))
B = float(input("Enter the breath of a rectangle:"))

def perimeter():
    P = 2 * (L + B)
    print("Perimeter of a rectangle:", P)

def area():
    A = L * B
    print("Area of a rectangle:", A)

perimeter()
area()
