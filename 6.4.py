# Create a list of tuples containing (food_item, price)
food_items = [
    ("Pizza", 12.99),
    ("Burger", 8.50),
    ("Salad", 7.25),
    ("Steak", 25.00),
    ("Ice Cream", 5.75)
]

print("Original food items list:")
for item in food_items:
    print(f"{item[0]}: ${item[1]}")

# Sort the tuples in descending order by price
sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("\nFood items sorted by price (descending):")
for item in sorted_food_items:
    print(f"{item[0]}: ${item[1]}")
