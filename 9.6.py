def create_power_tuples(end_value):
    # Create a list of tuples (x, x^2, x^3) for values from 1 to end_value
    result = [(x, x**2, x**3) for x in range(1, end_value + 1)]
    return result

# Test the function
end = 10
power_list = create_power_tuples(end)

print(f"List of tuples (x, x^2, x^3) from 1 to {end}:")
for item in power_list:
    print(f"{item[0]}: {item}")
