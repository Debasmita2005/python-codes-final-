# Create two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

print("First list:", list1)
print("Second list:", list2)

# Add corresponding elements using map and lambda
result = list(map(lambda x, y: x + y, list1, list2))

print("Result after adding corresponding elements:", result)

# Alternative approach using list comprehension (not using map/lambda)
result_alt = [list1[i] + list2[i] for i in range(len(list1))]
print("Same result using list comprehension:", result_alt)
