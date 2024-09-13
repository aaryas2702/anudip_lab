def find_largest_and_smallest(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None

    # Initialize the largest and smallest values
    largest = numbers[0]
    smallest = numbers[0]

    # Iterate through the list to find the largest and smallest
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage
numbers = [32, 51, 41, 68, 27, 2]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
