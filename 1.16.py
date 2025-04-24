#This program calculates simple interest
def SI():
    P = float(input("Enter the principal amount:"))
    R = float(input("Enter rate of interest:"))
    N = float(input("Enter time periods:"))
    I = P * R * N / 100
    print("Simple Interest:", I)

SI()
