#This program prints largest and smallest values out of three
a = float(input("Enter first value:"))
b = float(input("Enter second value:"))
c = float(input("Enter third value:"))

def large():
       if a>b and a>c:
              l = a
       elif b>a and b>c:
               l = b
       else:
              l = c
       print(l, "is the largest number")

def small():
       if a<b and a<c:
              s = a
       elif b<a and b<c:
               s = b
       else:
              s = c
       print(s, "is the smallest number")
       
large()
small()
