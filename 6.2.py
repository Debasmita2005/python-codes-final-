# List of tuples containing (roll_no, name, age)
students = [(101, "Alice", 15), (102, "Bob", 16), (103, "Charlie", 15), (104, "Diana", 16)]

# Create three separate lists
roll_numbers = []
names = []
ages = []

# Extract data into separate lists
for student in students:
    roll_numbers.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Original student data:", students)
print("Roll numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)

# Alternative approach using list comprehension
roll_numbers_alt = [student[0] for student in students]
names_alt = [student[1] for student in students]
ages_alt = [student[2] for student in students]

print("\nUsing list comprehension:")
print("Roll numbers:", roll_numbers_alt)
print("Names:", names_alt)
print("Ages:", ages_alt)
