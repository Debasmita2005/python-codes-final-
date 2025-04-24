import datetime

# Create two date tuples (d, m, y)
date1 = (10, 5, 2023)
date2 = (15, 8, 2023)

print(f"First date (DD-MM-YYYY): {date1[0]}-{date1[1]}-{date1[2]}")
print(f"Second date (DD-MM-YYYY): {date2[0]}-{date2[1]}-{date2[2]}")

# Convert tuples to datetime objects
datetime1 = datetime.datetime(date1[2], date1[1], date1[0])
datetime2 = datetime.datetime(date2[2], date2[1], date2[0])

# Calculate the difference in days
days_difference = abs((datetime2 - datetime1).days)

print(f"Number of days between the two dates: {days_difference}")
