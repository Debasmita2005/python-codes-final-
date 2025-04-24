#This program converts number 0 to 19 to its equivalent words
a = int(input("Enter number:"))

def words():
    if a == 0:
        print("Zero")
    elif a == 1:
        print("One")
    elif a == 2:
        print("Two")
    elif a == 3:
        print("Three")
    elif a == 4:
        print("Four")
    elif a == 5:
        print("Five")
    elif a == 6:
        print("Six")
    elif a == 7:
        print("Seven")
    elif a == 8:
        print("Eight")
    elif a == 9:
        print("Nine")
    elif a == 10:
        print("Ten")
    elif a == 11:
        print("Eleven")
    elif a == 12:
        print("Twelve")
    elif a == 13:
        print("Thirteen")
    elif a == 14:
        print("Fourteen")
    elif a == 15:
        print("Fifteen")
    elif a == 16:
        print("Sixteen")
    elif a == 17:
        print("Seventeen")
    elif a == 18:
        print("Eighteen")
    elif a == 19:
        print("Nineteen")
    else:
        print("Number is out of range")

words()
