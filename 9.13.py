def binary_equivalent(n):
    # Base case
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # Recursive case: convert n//2 to binary and append n%2
        return binary_equivalent(n // 2) + str(n % 2)

# Test the function
for num in range(10, 21):
    print(f"Binary equivalent of {num}: {binary_equivalent(num)}")

# Function to get user input and find binary equivalent
def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Please enter a positive integer.")
            return
        
        binary = binary_equivalent(num)
        print(f"Binary equivalent of {num}: {binary}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Uncomment to run with user input
# main()
