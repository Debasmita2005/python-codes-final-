# Function to calculate character frequency
def char_frequency(input_string):
    # Create an empty dictionary
    freq_dict = {}
    
    # Count each character
    for char in input_string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict

# Get input from user
user_input = input("Enter a string: ")

# Calculate frequency
result = char_frequency(user_input)

# Display the result
print("\nCharacter frequency:")
for char, count in result.items():
    print(f"'{char}': {count}")

# Alternative approach using collections.Counter
print("\nAlternative approach using Counter:")
from collections import Counter
counter_result = Counter(user_input)
for char, count in counter_result.items():
    print(f"'{char}': {count}")
