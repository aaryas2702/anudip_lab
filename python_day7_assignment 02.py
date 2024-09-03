def is_armstrong_number(number):
    # Convert number to string to iterate over digits
    num_str = str(number)
    
    # Determine the number of digits
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum equals the original number
    return sum_of_powers == number

# Input number
try:
    input_number = int(input("Enter a number to check if it's an Armstrong number: "))
    
    # Check if the input number is an Armstrong number
    if is_armstrong_number(input_number):
        print(f"{input_number} is an Armstrong number.")
    else:
        print(f"{input_number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")

#output

    Enter a number to check if it's an Armstrong number: 153
    153 is an Armstrong number.

   Enter a number to check if it's an Armstrong number: 8976
   8976 is not an Armstrong number. 
