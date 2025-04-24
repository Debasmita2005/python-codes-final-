#Write a program to create a csv file that we can directly open in MS-Excel.

import csv
data = [["Roll No", "Name", "Subject1", "Subject2"], [1, "sakshi", 78, 85], [2, "krutika", 88, 72],[3, "ayushi", 70, 68]]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created successfully!")
