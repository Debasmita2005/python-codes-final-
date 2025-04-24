# List of faculty member names
faculty_names = ["Dr. Smith", "Professor Johnson", "Ms. Williams", "Dr. Brown", "Professor Richardson", "Mr. Lee", "Dr. Elizabeth Thompson"]

print("List of faculty members:")
for name in faculty_names:
    print(f"- {name}")

# Filter names with length > 8 using filter and lambda
long_names = list(filter(lambda name: len(name) > 8, faculty_names))

print("\nFaculty members with names longer than 8 characters:")
for name in long_names:
    print(f"- {name} (length: {len(name)})")

# Alternative using list comprehension
long_names_alt = [name for name in faculty_names if len(name) > 8]
print("\nSame result using list comprehension:", long_names_alt)

# Count the names
print(f"\nOut of {len(faculty_names)} faculty members, {len(long_names)} have names longer than 8 characters.")
