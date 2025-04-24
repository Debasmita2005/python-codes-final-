def sanitize_list(lst, index=0):
    # Base case: reached the end of the list
    if index >= len(lst):
        return lst
    
    # If current element is negative, replace with 0
    if lst[index] < 0:
        lst[index] = 0
    
    # Recursively process the rest of the list
    return sanitize_list(lst, index + 1)

# Test the function
numbers = [5, -2, 10, -7, 0, 15, -30, 8]
print(f"Original list: {numbers}")
sanitized = sanitize_list(numbers.copy())  # Copy to keep original
print(f"Sanitized list: {sanitized}")

another_list = [-5, -10, -15, 20, 25]
print(f"\nOriginal list: {another_list}")
sanitized2 = sanitize_list(another_list.copy())
print(f"Sanitized list: {sanitized2}")
