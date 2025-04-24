# List with boys names as tuples and girls names as strings
student_list = ["Emma", ("John",), "Sophia", ("Michael",), "Olivia", ("Daniel",), ("Matthew",), "Ava"]

# Count boys and girls
boys_count = 0
girls_count = 0

for student in student_list:
    if isinstance(student, tuple):
        boys_count += 1
    else:
        girls_count += 1

print("List of students:", student_list)
print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")
