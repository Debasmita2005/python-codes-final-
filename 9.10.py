def frequency(string):
    # Split the string into words
    words = string.split()
    
    # Create a dictionary to store word frequencies
    freq_dict = {}
    
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    # Sort by words
    sorted_freq = {word: freq_dict[word] for word in sorted(freq_dict)}
    
    return sorted_freq

# Test the function
test_string = "the quick brown fox jumps over the lazy dog the fox is quick"
result = frequency(test_string)

print(f"String: '{test_string}'")
print("Word frequencies (sorted by word):")
for word, count in result.items():
    print(f"'{word}': {count}")
