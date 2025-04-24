# Create three separate dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)

# Method 1: Using update() method
dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

print("\nConcatenated dictionary (using update()):", dict4)

# Method 2: Using dictionary unpacking (Python 3.5+)
dict4_alt = {**dict1, **dict2, **dict3}
print("Concatenated dictionary (using unpacking):", dict4_alt)

# Method 3: Using the | operator (Python 3.9+)
# dict4_newer = dict1 | dict2 | dict3
# print("Concatenated dictionary (using | operator):", dict4_newer)
