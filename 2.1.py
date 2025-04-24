#This program prints largest and smallest values out of two
a = float(input("Enter one value:"))
b = float(input("Enter another value:"))

def compare():
       if a>b:
              print(a, "is the largest number")
              print(b, "is the smallest number")
       else:
              print(b, "is the largest number")
              print(a, "is the smallest number")

compare()
