#This program prints all the alphabet in upper case and in lower case

def upper():
    print("Alphabet in upper case:")
    for i in range(65,91):
        print(chr(i), end=' ')

def lower():
    print("\nAlphabet in lower case:")
    for i in range(97,123):
        print(chr(i), end=' ')

upper()
lower()
