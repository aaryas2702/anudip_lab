def check_number(number):
    """
    Determine if a number is positive, negative, or zero.

    Parameters:
    number (float): The number to check.

    Returns:
    str: A message indicating whether the number is positive, negative, or zero.
    """
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."

def main():
    try:
        # Prompt the user for input
        user_input = float(input("Enter a number: "))
        
        # Check and print whether the number is positive, negative, or zero
        result = check_number(user_input)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
#output
    Enter a number: 34
    The number is positive.

    Enter a number: -9
    The number is negative.


    
