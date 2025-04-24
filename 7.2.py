# Create dictionaries for testing
empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

# Method 1: Using len() function
if len(empty_dict) == 0:
    print("Method 1: The dictionary is empty")
else:
    print("Method 1: The dictionary is not empty")

if len(non_empty_dict) == 0:
    print("Method 1: The dictionary is empty")
else:
    print("Method 1: The dictionary is not empty")

# Method 2: Direct boolean evaluation
if not empty_dict:
    print("Method 2: The dictionary is empty")
else:
    print("Method 2: The dictionary is not empty")

if not non_empty_dict:
    print("Method 2: The dictionary is empty")
else:
    print("Method 2: The dictionary is not empty")

# Function to check if dictionary is empty
def is_empty(dictionary):
    return len(dictionary) == 0

# Test the function
print("\nUsing function:")
print(f"Empty dictionary is empty: {is_empty(empty_dict)}")
print(f"Non-empty dictionary is empty: {is_empty(non_empty_dict)}")
