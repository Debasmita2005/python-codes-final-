#This program generate random odd and even number's lists and replace third element of odd list by even list and then flatten, sort and print the list
import random
odd_l = random.sample(range(1, 100, 2), 5)
even_l = random.sample(range(2, 101, 2), 4)

def list_operation():
    print(f"List of 5 odd random numbers:{odd_l}")
    print(f"List of 4 even random numbers:{even_l}")
    flatten_l  = odd_l.copy()
    flatten_l[2:3] = even_l
    print(f"Flattened list by replacing third element of odd number list:{flatten_l}")
    flatten_l.sort()
    print(f"Sorted flattened list:{flatten_l}")

list_operation()
