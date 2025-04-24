def reverse_list(lst):
    # Base case: empty list or single element
    if not lst or len(lst) == 1:
        return lst
    
    # Recursive case: first element goes to the end
    return reverse_list(lst[1:]) + [lst[0]]

# Test the function
numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")
print(f"Reversed list: {reverse_list(numbers)}")

another_list = [10, 20, 30, 40, 50, 60]
print(f"\nOriginal list: {another_list}")
print(f"Reversed list: {reverse_list(another_list)}")
