#This prrogram print N natural numbers in reverse
n = int(input("Enter a number:"))

def print_reverse():
    for i in range(n, 0, -1):
        print(i)

print_reverse()
