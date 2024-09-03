def count_characters(input_string):
    # Initialize counters for letters, digits, and special symbols
    letter_count = 0
    digit_count = 0
    special_count = 0

    # Iterate through each character in the string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            letter_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digit_count += 1
        else:  # If it's neither a letter nor a digit, it's a special symbol
            special_count += 1

    # Print the counts
    print(f"Total letters: {letter_count}")
    print(f"Total digits: {digit_count}")
    print(f"Total special symbols: {special_count}")

# Example usage
input_string = "P@#yn26at^&i5ve"
count_characters(input_string)


#output
Total letters: 8
Total digits: 3
Total special symbols: 4
