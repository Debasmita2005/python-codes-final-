#This program print factorial of a given number
n = int(input("Enter a number:"))

def factorial():
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"Factorial of {n} is {fact}")

factorial()
