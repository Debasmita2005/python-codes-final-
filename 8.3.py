# Create an empty set
name_set = set()
print("Initial empty set:", name_set)

# Add five new names to the set
name_set.add("John")
name_set.add("Emma")
name_set.add("Michael")
name_set.add("Sophia")
name_set.add("Daniel")

print("After adding 5 names:", name_set)

# Modify one existing name
# Note: Sets don't support direct modification, so we need to remove and add
name_to_modify = "Emma"
modified_name = "Emily"

if name_to_modify in name_set:
    name_set.remove(name_to_modify)
    name_set.add(modified_name)
    print(f"Modified '{name_to_modify}' to '{modified_name}'")

print("After modification:", name_set)

# Delete two names from the set
names_to_delete = ["Michael", "Daniel"]

for name in names_to_delete:
    if name in name_set:
        name_set.remove(name)
        print(f"Deleted '{name}'")

print("Final set after deletions:", name_set)
