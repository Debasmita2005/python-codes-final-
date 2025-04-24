#This program determine the position of a point with respect to circle
r = int(input("Enter value of radius of the circle:"))
x = int(input("Enter value of x cordinate of the point:"))
y = int(input("Enter value of y cordinate of the point:"))

def position():
    if pow(x, 2) + pow (y, 2) < pow(r, 2):
        print("Point is inside the circle")
    elif pow(x, 2) + pow (y, 2) > pow(r, 2):
        print("Point is outside the circle")
    else:
        print("Point is on the circle")

position()
