def ispangram(string):
    # Convert to lowercase and create a set of alphabets in the string
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Remove all non-alphabetic characters and convert to set
    string_set = set(char.lower() for char in string if char.isalpha())
    
    # Check if alphabet is a subset of the string set
    return alphabet <= string_set

# Test cases
test1 = "The quick brown fox jumps over the lazy dog"
test2 = "Crazy Fredrick bought many very exquisite opal jewels"
test3 = "Hello World"

print(f"'{test1}' is a pangram: {ispangram(test1)}")
print(f"'{test2}' is a pangram: {ispangram(test2)}")
print(f"'{test3}' is a pangram: {ispangram(test3)}")
