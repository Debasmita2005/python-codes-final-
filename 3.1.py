#This program counts vowels in the string
str1 = input("Enter a string:")

def count_vowels():
    c = 0
    for i in str1:
        if i in "AEIOUaeiou":
            c += 1
    print(c, "vowels are present in the string")

count_vowels()
        
