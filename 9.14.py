def count_vowels(string, index=0):
    # List of vowels
    vowels = 'aeiouAEIOU'
    
    # Base case: reached the end of string
    if index >= len(string):
        return 0
    
    # Check if current character is a vowel
    if string[index] in vowels:
        return 1 + count_vowels(string, index + 1)
    else:
        return count_vowels(string, index + 1)

# Test the function
test_string = "Hello World"
print(f"Number of vowels in '{test_string}': {count_vowels(test_string)}")

test_string = "Python Programming"
print(f"Number of vowels in '{test_string}': {count_vowels(test_string)}")

# Function to get user input and count vowels
def main():
    text = input("Enter a string: ")
    vowel_count = count_vowels(text)
    print(f"Number of vowels in '{text}': {vowel_count}")

# Uncomment to run with user input
# main()
