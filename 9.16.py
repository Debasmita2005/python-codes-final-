def power(a, b):
    # Base cases
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / power(a, -b)
    
    # Recursive case
    return a * power(a, b - 1)

# Test the function
base = 2
exponent = 5
print(f"{base}^{exponent} = {power(base, exponent)}")

base = 3
exponent = 4
print(f"{base}^{exponent} = {power(base, exponent)}")

# Handle negative exponent
base = 2
exponent = -3
print(f"{base}^{exponent} = {power(base, exponent)}")

# Function to get user input and calculate power
def main():
    try:
        a = float(input("Enter base (a): "))
        b = int(input("Enter exponent (b): "))
        
        result = power(a, b)
        print(f"{a}^{b} = {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Uncomment to run with user input
# main()
