#This program print the multiplication table of the given number
n = int(input("Enter an integer number:"))

def table():
    for i in range(1,11):
        m = n * i
        print(f"{n}*{i}={m}")

table()
