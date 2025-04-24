#This program removes one string from another if present
str1 = input("Enter first string:")
str2 = input("Enter second string:")

def remove_string():
    str3 = ""
    if str2 in str1:
        n = str1.find(str2)
        str3 = str1[:n] + str1[n + len(str2):]
        print(f"Resultant string:{str3}")
    else:
        print(f"'{str2}' is not present in '{str1}'")

remove_string()
