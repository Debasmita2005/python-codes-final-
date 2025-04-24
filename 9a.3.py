import random

# Generate 10 different random numbers between -15 and 15
random_numbers = []
while len(random_numbers) < 10:
    num = random.randint(-15, 15)
    if num not in random_numbers:
        random_numbers.append(num)

print("Original list of 10 random numbers:", random_numbers)

# Create a new list with squares using map and lambda
squares = list(map(lambda x: x**2, random_numbers))
print("Squares:", squares)

# Alternative using list comprehension
squares_alt = [x**2 for x in random_numbers]
print("Squares (using list comprehension):", squares_alt)

# Using the built-in pow function with map
squares_pow = list(map(lambda x: pow(x, 2), random_numbers))
print("Squares (using pow function):", squares_pow)
