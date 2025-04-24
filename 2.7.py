#This program check that year is leap year or not
a = int(input("Enter a year:"))

def year():
    if a % 4 == 0:
        print(a, "is laep year")
    else:
        print(a, "is not leap year")

year()
