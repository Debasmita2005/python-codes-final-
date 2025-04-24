def string_length(s, index=0):
    # Base case: empty string
    if index >= len(s):
        return 0
    
    # Recursive case: count this character plus rest of string
    return 1 + string_length(s, index + 1)

# Test the function
test_string = "Hello World"
print(f"String: '{test_string}'")
print(f"Length: {string_length(test_string)}")

another_string = "Python Programming"
print(f"\nString: '{another_string}'")
print(f"Length: {string_length(another_string)}")

# Compare with built-in len() function
print(f"Built-in length: {len(another_string)}")
