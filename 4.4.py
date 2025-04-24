#This program check whether a given number is prime, perfect, armstrong, palindrome and automorphic
n = int(input("Enter a number:"))

def isprime():
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is prime number")
    else:
        print(f"{n} is not a prime number")

def isperfect():
    if n > 1:
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        if total == n:
            print(f"{n} is a perfect number")
        else:
            print(f"{n} is not a perfect number")
    else:
        print(f"{n} is not a perfect number")

def isarmstrong():
    if n > 0:
        s = str(n)
        p = len(s)
        total = 0
        for i in range(p):
            total += int(s[i]) ** p
        if total == n:
            print(f"{n} is an armstrong number")
        else:
            print(f"{n} is not an armstrong number")
    else:
        print(f"{n} is not an armstrong number")

def ispalindrome():
    if n >= 0:
        n1 = str(n)
        n2 = n1[::-1]
        if n1 == n2:
            print(f"{n} is a palindrome number")
        else:
            print(f"{n} is not a palindrome number")
    else:
        print(f"{n} is not a palindrome number")

def isautomorphic():
    if n >= 0:
        s = str(n)
        m = str(n ** 2)
        if m.endswith(s):
            print(f"{n} is an automorphic number")
        else:
            print(f"{n} is not an automorphic number")
    else:
        print(f"{n} is not an automorphic number")

isprime()
isperfect()
isarmstrong()
ispalindrome()
isautomorphic()
