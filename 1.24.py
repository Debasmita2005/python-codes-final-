#This program swaps two numbers
def swap():
      a = float(input("Enter a number:"))
      b = float(input("Enter another number:"))
      print("Before:",a,b)
      a, b = b, a
      print("After:",a,b)

swap()
