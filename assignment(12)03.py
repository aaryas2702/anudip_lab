def find_duplicates(numbers):
    # Dictionary to store the count of each number
    count_dict = {}
    duplicates = []

    # Count occurrences of each number
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    # Find numbers with more than one occurrence and add to duplicates list
    for number, count in count_dict.items():
        if count > 1:
            # Add the duplicate value multiple times (as many as its occurrences minus one)
            duplicates.extend([number] * (count - 1))

    return duplicates

# Example usage
numbers = [51, 42, 23, 14, 65, 42, 46, 17, 23, 98, 51]
duplicates = find_duplicates(numbers)
print("Duplicate values:", duplicates)
Duplicate values: [51, 42, 23]
