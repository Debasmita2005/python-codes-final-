#This program evaluates result of three subjects
print("Enter marks")
m1 = float(input("First subject:"))
m2 = float(input("Second subject:"))
m3 = float(input("Third subject:"))

def average():
    total = m1 + m2 + m3
    print("Total marks:", total)
    avg = total / 3
    print("Average marks:", avg)

def pass_fail():
    if all(x >= 39 for x in [m1, m2, m3]):
        print("You are pass")
    else:
        print("You are fail")

def grades(m):
    if m == 'Absent':
        grade = 'NA'
    m = int(m)
    if 0 <= m <= 39:
        grade = 'F'
    elif 40 <= m <= 44:
        grade = 'P'
    elif 45 <= m <= 49:
        grade = 'C'
    elif 50 <= m <= 54:
        grade = 'B'
    elif 55 <= m <= 59:
        grade = 'B+'
    elif 60 <= m <= 69:
        grade = 'A'
    elif 70 <= m <= 79:
        grade = 'A+'
    elif 80 <= m <= 100:
        grade = 'O'
    else:
        grade = 'Invalid marks'

    print('Grade for subject:', grade)


average()
pass_fail()
for i in [m1, m2, m3]:
    grades(i)
