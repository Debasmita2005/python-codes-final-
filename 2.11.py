#This program check if three points fall on one straight 
print("Enter first point:")
x1 = float(input())
y1 = float(input())
print("Enter second point:")
x2 = float(input())
y2 = float(input())
print("Enter third point:")
x3 = float(input())
y3 = float(input())

def linearity():
    l = x1 * (y2 - y3) - x2 * (y1 - y3) + x3 * (y1 - y2)
    if l == 0:
        print("All the three points fall on one straight line")
    else:
        print("All the three points does not fall on one straight line")

linearity()
