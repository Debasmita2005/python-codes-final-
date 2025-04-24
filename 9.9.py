def count_alpha_digits(string):
    alpha_count = 0
    digit_count = 0
    
    for char in string:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
    
    return {"alphabets": alpha_count, "digits": digit_count}

# Test the function
test_string = "Hello123 World456!"
result = count_alpha_digits(test_string)

print(f"String: '{test_string}'")
print(f"Number of alphabets: {result['alphabets']}")
print(f"Number of digits: {result['digits']}")

# Another example
another_string = "Python3.9 is awesome! Released in 2020."
result2 = count_alpha_digits(another_string)

print(f"\nString: '{another_string}'")
print(f"Number of alphabets: {result2['alphabets']}")
print(f"Number of digits: {result2['digits']}")
