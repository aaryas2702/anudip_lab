def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]

# Input from the user
try:
    num = int(input("Enter a number to check if it's a palindrome: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
#outout
    Enter a number to check if it's a palindrome: 65
65 is not a palindrome.

    Enter a number to check if it's a palindrome: 22
22 is a palindrome.
       
    
