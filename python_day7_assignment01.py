def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]

# Input string
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


