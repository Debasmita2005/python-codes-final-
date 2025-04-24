#This program generate N number of Fibonacci series
n = int(input("Enter a number:"))

def fibonacci():
    if n >= 2:
        a, b = 0, 1
        print(f"Fibonacci series of {n} number:")
        print(a)
        print(b)
        for i in range(n - 2):
            c = a + b
            print(c)
            a = b
            b = c
    else:
        print("Fibonacci series contains atleast two terms")

fibonacci()
