# List containing some empty tuples
tuple_list = [(1, 2), (), (3, 4, 5), (), (6,), (), (7, 8)]
print("Original list:", tuple_list)

# Remove empty tuples
filtered_list = [tup for tup in tuple_list if tup]
print("List after removing empty tuples:", filtered_list)

# Alternative approach
filtered_list_alt = list(filter(None, tuple_list))
print("Alternative method result:", filtered_list_alt)
