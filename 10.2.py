#Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.

import csv
students = {}

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        rollno = int(row[0])
        name = row[1]
        marks = list(map(int, row[2:]))
        total = sum(marks)     
        students[rollno] = { "name": name, "marks": marks, "total": total}

for roll, info in students.items():
    print(f"Roll No: {roll}, Name: {info['name']}, Marks: {info['marks']}, Total: {info['total']}")
