def convert(string):
    # Split the string into words
    words = string.split()
    
    # Remove duplicates by converting to set, then sort
    unique_sorted = sorted(set(words))
    
    # Join back into a string
    result = ' '.join(unique_sorted)
    
    return result

# Test the function
test_string = "hello world hello python world programming python code"
result = convert(test_string)

print(f"Original string: '{test_string}'")
print(f"After removing duplicates and sorting: '{result}'")
