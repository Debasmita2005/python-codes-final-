#This program calculate area & perimeter of a square 
L = float(input("Enter the lenght of a square:"))

def perimeter():
    P = 4 * L
    print("Perimeter of a square:", P)

def area():
    A = L ** 2
    print("Area of a square:", A)

perimeter()
area()
