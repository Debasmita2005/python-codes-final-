#This program converts convert all characters of a string into lower case, upper case and toggle case
str1 = input("Enter a string:")

def convert_lower():
    lower = ""
    for c in str1:
        if 'A' <= c <= 'Z':
            lower += chr(ord(c) + 32)
        else:
            lower += c
    print("Lower Case:", lower)

def convert_upper():
    upper = ""
    for c in str1:
        if 'a' <= c <= 'z':
            upper += chr(ord(c) - 32)
        else:
            upper += c
    print("Upper Case:", upper)

def convert_toggle():
    toggle = ""
    for c in str1:
        if 'A' <= c <= 'Z':
            toggle += chr(ord(c) + 32)
        elif 'a' <= c <= 'z':
            toggle += chr(ord(c) - 32)
        else:
            toggle += c
    print("Toggle Case:", toggle)

convert_lower()
convert_upper()
convert_toggle()
        
