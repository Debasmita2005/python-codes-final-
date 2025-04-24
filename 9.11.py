def create_list(list1, list2):
    # Find intersection of two lists
    intersection = [item for item in list1 if item in list2]
    return intersection

# Test the function
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]

result = create_list(list_a, list_b)

print(f"List 1: {list_a}")
print(f"List 2: {list_b}")
print(f"Intersection: {result}")

# Alternative using set intersection
def create_list_alt(list1, list2):
    return list(set(list1).intersection(set(list2)))

result_alt = create_list_alt(list_a, list_b)
print(f"Intersection (using set): {result_alt}")
