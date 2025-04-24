#This program generate list of 30 random numbers and seperate them in +ve and -ve list
import random
a = [random.randint(-100, 100) for x in range(30)]

def seperate():
    p = [i for i in a if i >= 0]
    n = [i for i in a if i < 0]
    print(f"Original list:{a}")
    print(f"Positive list:{p}")
    print(f"Negative list:{n}")
    
seperate()
