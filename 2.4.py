#This program check that given number is divisible by 10 or not
a = float(input("Enter a number:"))

def div():
    if a % 10 == 0:
        print(a, "is divisible by 10")
    else:
        print(a, "is not divisible by 10")

div()
