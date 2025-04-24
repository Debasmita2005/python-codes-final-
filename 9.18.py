def sum_list(lst, index=0):
    # Base case: reached the end of the list
    if index >= len(lst):
        return 0
    
    # Recursive case: add current element to sum of rest
    return lst[index] + sum_list(lst, index + 1)

def average_list(lst):
    if not lst:
        return 0
    
    # Calculate sum recursively, then divide by length
    total = sum_list(lst)
    return total / len(lst)

# Test the function
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"Average: {average_list(numbers)}")

another_list = [5, 15, 25, 35, 45, 55]
print(f"\nList: {another_list}")
print(f"Average: {average_list(another_list)}")
