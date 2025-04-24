#This program converts 5 strings in list to uppercase
strings_l = list(map(str, input("Enter five strings separated by space:").split()))
'''for i in range(5):
    string = input("Enter a string:")
    strings_l.append(string)'''

def upper():
    if len(strings_l) == 5:
        print(f"Original list of strings:{strings_l}")
        for i in range(5):
            strings_l[i] = strings_l[i].upper()
        print(f"Modified list of strings:{strings_l}")
    else:
        print("Invalid input")

upper()
