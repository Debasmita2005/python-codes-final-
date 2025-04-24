# Dictionary containing grocery items and their prices
prices = {
    'apple': 1.50,
    'banana': 0.75,
    'milk': 2.25,
    'bread': 2.00,
    'eggs': 3.50,
    'cheese': 4.75,
    'rice': 1.80
}

# Dictionary containing grocery items and quantity purchased
quantities = {
    'apple': 6,
    'banana': 4,
    'milk': 2,
    'bread': 1,
    'eggs': 1,
    'cheese': 0.5,  # Half kg or package
    'rice': 2
}

print("Grocery Items Prices:")
for item, price in prices.items():
    print(f"{item}: ${price:.2f}")

print("\nQuantities Purchased:")
for item, qty in quantities.items():
    print(f"{item}: {qty}")

# Calculate the total bill
total_bill = 0
bill_details = []

print("\nBill Details:")
print("-" * 40)
print(f"{'Item':<10} {'Price':<8} {'Quantity':<10} {'Amount':<10}")
print("-" * 40)

for item, quantity in quantities.items():
    if item in prices:
        price = prices[item]
        amount = price * quantity
        total_bill += amount
        bill_details.append((item, price, quantity, amount))
        print(f"{item:<10} ${price:<7.2f} {quantity:<10} ${amount:<9.2f}")

print("-" * 40)
print(f"{'Total':<30} ${total_bill:.2f}")
