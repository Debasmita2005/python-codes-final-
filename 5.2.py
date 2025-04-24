#This program generate 20 random number of list and then print position of all occurrences of the number accepted from user
import random
lst = [random.randint(0, 100) for x in range(20)]
a = int(input("Enter an integer number less than 100:"))

def position():
    result = False
    if 0 <= a <= 100:
        for i,n in enumerate(lst):
            if a == n:
                print(f"Position of {a} in list:{i}")
                result = True
        if not result:
            print(f"{a} is not found in list")
        print(f"List of 20 random numbers:{lst}")
    else:
        print("Invalid input")

position()
