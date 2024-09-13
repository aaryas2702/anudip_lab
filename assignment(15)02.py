# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get the symmetric difference of both sets
unique_elements = set1.symmetric_difference(set2)

# Alternatively, we can use the ^ operator to achieve the same result:
# unique_elements = set1 ^ set2

# Print the result
print(unique_elements)

#output
{20, 70, 10, 60}
