# Create a tuple
original_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", original_tuple)

# Tuples are immutable, so we can't modify elements directly
# We need to convert to a list, modify, and convert back to a tuple

# Convert to list
temp_list = list(original_tuple)

# Modify the element (e.g., change 30 to 35)
index_to_modify = 2
new_value = 35
temp_list[index_to_modify] = new_value

# Convert back to tuple
modified_tuple = tuple(temp_list)
print(f"After modifying element at index {index_to_modify} to {new_value}:")
print("Modified tuple:", modified_tuple)

# Alternative method: create a new tuple from slices
position = 2
new_element = 38
alternative_modified = original_tuple[:position] + (new_element,) + original_tuple[position+1:]
print("\nAlternative approach:")
print("Modified tuple:", alternative_modified)
