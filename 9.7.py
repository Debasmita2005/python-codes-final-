def ispalindrome(string):
    # Remove spaces and convert to lowercase
    processed_string = ''.join(string.lower().split())
    
    # Check if the string equals its reverse
    return processed_string == processed_string[::-1]

# Test cases
test1 = "A man a plan a canal Panama"
test2 = "Race car"
test3 = "No lemon, no melon"
test4 = "Hello World"

print(f"'{test1}' is a palindrome: {ispalindrome(test1)}")
print(f"'{test2}' is a palindrome: {ispalindrome(test2)}")
print(f"'{test3}' is a palindrome: {ispalindrome(test3)}")
print(f"'{test4}' is a palindrome: {ispalindrome(test4)}")
