#This program calculate average of three subjects along with their total
m1 = float(input("Enter the marks of first subject:"))
m2 = float(input("Enter the marks of second subject:"))
m3 = float(input("Enter the marks of third subject:"))

def average():
    sum = m1 + m2 + m3
    print("Total marks:", sum)
    avg = sum / 3
    print("Average marks:", avg)

average()
