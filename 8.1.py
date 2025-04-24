# List of words
word_list = ["apple", "banana", "orange", "grape", "kiwi", "banana", "apple", "mango"]
print("Original list:", word_list)

# Convert words to uppercase and store in a set
uppercase_set = set(word.upper() for word in word_list)

# Display the result
print("Set with uppercase words:", uppercase_set)
print(f"Number of unique words: {len(uppercase_set)}")

# Note: Duplicates like "apple" and "banana" appear only once in the set
