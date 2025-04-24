#This program checks whether one string is there in another string
str1 = input("Enter first string:")
str2 = input("Enter second string:")

def check_string():
    if str1 in str2:
        print(f"First string '{str1}' is in the second string '{str2}'")
    elif str2 in str1:
        print(f"Second string '{str2}' is in the first string '{str1}'")
    else:
        print("Neither string is contained within another")

check_string()
