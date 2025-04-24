def find_prime_factors(n, i=2, factors=None):
    if factors is None:
        factors = []
    
    # Base case: n is 1 or less
    if n <= 1:
        return factors
    
    # If i divides n, add i to factors and recurse with n/i
    if n % i == 0:
        factors.append(i)
        return find_prime_factors(n // i, i, factors)
    
    # If i doesn't divide n, try next number
    return find_prime_factors(n, i + 1, factors)

# Test the function
number = 84
print(f"Prime factors of {number}: {find_prime_factors(number)}")

number = 123
print(f"Prime factors of {number}: {find_prime_factors(number)}")

# Function to get user input and find prime factors
def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return
        
        factors = find_prime_factors(num)
        print(f"Prime factors of {num}: {factors}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Uncomment to run with user input
# main()
