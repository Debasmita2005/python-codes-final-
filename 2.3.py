#This program prints the number is odd or even
a = int(input("Enter a number:"))

def odd_even():
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")

odd_even()
