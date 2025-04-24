def is_palindrome(item):
    # Convert item to string
    item_str = str(item)
    # Check if the string equals its reverse
    return item_str == item_str[::-1]

lst = ['madam', 'Python', "malayalam", 12321]
print("Original list:", lst)

# Filter palindromes using filter and lambda
palindromes = list(filter(lambda item: str(item) == str(item)[::-1], lst))
print("Palindromes (using filter and lambda):", palindromes)

# Alternative using list comprehension
palindromes_alt = [item for item in lst if str(item) == str(item)[::-1]]
print("Palindromes (using list comprehension):", palindromes_alt)

# Using the defined function with filter
palindromes_func = list(filter(is_palindrome, lst))
print("Palindromes (using custom function):", palindromes_func)
