#This program count number of alphabet and number of digit in string
str1 = input("Enter a string:")

def count():
    str2 = str1.lower()
    a, d = 0, 0
    for i in str2:
        if i in "abcdefghijklmnoupqrstuvwxyz":
            a += 1
        elif i in "0123456789":
            d += 1
    print(f"{a} alphabets and {d} digits are present in {str1}")

count()
