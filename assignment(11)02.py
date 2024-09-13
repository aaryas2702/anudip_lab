def get_integer_input():
    user_input = input("Please enter an integer: ")
    
    try:
        integer_value = int(user_input)
        print(f"The entered integer is: {integer_value}")
        
    except ValueError:
        raise ValueError("Invalid input: The input is not a valid integer.")

# Run the function
get_integer_input()

#output
    1) Please enter an integer: tk
     ValueError: Invalid input: The input is not a valid integer.

     2) Please enter an integer: 24
     The entered integer is: 24
