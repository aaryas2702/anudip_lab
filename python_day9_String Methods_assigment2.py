def remove_duplicates(input_string):
    # Initialize an empty set to keep track of seen characters
    seen = set()
    # Initialize an empty list to store characters of the result string
    result = []

    # Iterate through each character in the input string
    for char in input_string:
        if char not in seen:
            # Add the character to the result list and mark it as seen
            result.append(char)
            seen.add(char)

    # Join the list of characters into a string and return it
    return ''.join(result)

# Example usage
input_string = "String and String Function"
output_string = remove_duplicates(input_string)
print("Original string:", input_string)
print("String after removing duplicates:", output_string)
