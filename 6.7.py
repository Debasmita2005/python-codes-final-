# Create a tuple
original_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", original_tuple)

# Tuples are immutable, so we can't delete elements directly
# We need to convert to a list, delete, and convert back to a tuple

# Convert to list
temp_list = list(original_tuple)

# Delete the element (e.g., delete 30)
index_to_delete = 2
deleted_value = temp_list[index_to_delete]
del temp_list[index_to_delete]

# Convert back to tuple
modified_tuple = tuple(temp_list)
print(f"After deleting element at index {index_to_delete} (value: {deleted_value}):")
print("Modified tuple:", modified_tuple)

# Alternative method: create a new tuple from slices
position = 3  # Delete element at index 3 (value: 40)
alternative_modified = original_tuple[:position] + original_tuple[position+1:]
print("\nAlternative approach:")
print(f"After deleting element at index {position} (value: {original_tuple[position]}):")
print("Modified tuple:", alternative_modified)
