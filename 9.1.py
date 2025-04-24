def count_lower_upper(text):
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return {"uppercase": upper_count, "lowercase": lower_count}

# Test the function with sample strings
sample_string = "Hello World! How Are You?"
result = count_lower_upper(sample_string)

print(f"Sample string: '{sample_string}'")
print(f"Uppercase count: {result['uppercase']}")
print(f"Lowercase count: {result['lowercase']}")

# Try another example
another_string = "PYTHON is FUN and EASY to Learn!"
result2 = count_lower_upper(another_string)

print(f"\nSample string: '{another_string}'")
print(f"Uppercase count: {result2['uppercase']}")
print(f"Lowercase count: {result2['lowercase']}")
