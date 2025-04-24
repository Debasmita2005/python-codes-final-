import random

# Create a set containing 10 random numbers in the range 15 to 45
random_set = set()

while len(random_set) < 10:
    random_set.add(random.randint(15, 45))

print("Set with 10 random numbers:", random_set)

# Count numbers less than 30
less_than_30 = sum(1 for num in random_set if num < 30)
print(f"Numbers less than 30: {less_than_30}")

# Delete numbers greater than 35
numbers_to_remove = {num for num in random_set if num > 35}
random_set -= numbers_to_remove  # Set difference operation

print("After removing numbers greater than 35:", random_set)
print(f"Set now contains {len(random_set)} number(s)")
