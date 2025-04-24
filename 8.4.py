# Create a set containing names beginning with A or B
names_set = {"Alice", "Bob", "Andrew", "Barbara", "Alex", "Bill", "Bella", "Amanda"}
print("Original set of names:", names_set)

# Create two empty sets for names beginning with A and B
a_names = set()
b_names = set()

# Separate names based on first letter
for name in names_set:
    if name.startswith('A'):
        a_names.add(name)
    elif name.startswith('B'):
        b_names.add(name)

print("\nNames beginning with 'A':", a_names)
print("Names beginning with 'B':", b_names)

# Alternative approach using set comprehension
a_names_alt = {name for name in names_set if name.startswith('A')}
b_names_alt = {name for name in names_set if name.startswith('B')}

print("\nUsing set comprehension:")
print("Names beginning with 'A':", a_names_alt)
print("Names beginning with 'B':", b_names_alt)
