#This program check that the area of the rectangle is greater than its perimeter
l = float(input("Enter length of rectangle:"))
b = float(input("Enter breadth of rectangle:"))

def compare():
    area = l * b
    perimeter = 2 * (l + b)
    if area > perimeter:
        print("The area of the rectangle is greater than its perimeter")
    elif area < perimeter:
        print("The area of the rectangle is not greater than its perimeter")
    else:
        print("The area of the rectangle is equal its perimeter")

compare()
