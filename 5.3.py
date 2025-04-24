#This program generate 50 random numbers in the range 1 and 30 and remove all duplicate values from the list
import random
a = [random.randint(1, 30) for x in range(50)]

def duplicate():
    i = 0
    print(f"Original list:{a}")
    while i < len(a):
        if a[i] in a[:i]:
            del(a[i])
        else:
            i += 1
    print(f"Unique valued list:{a}")
        
duplicate()
