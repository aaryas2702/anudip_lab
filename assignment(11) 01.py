def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        result = numerator / denominator
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    except ValueError:
        print("Error: Please enter valid numbers.")
        
    else:
        print(f"The result of dividing {numerator} by {denominator} is {result}.")

# Run the function
divide_numbers()

#output
      Enter the numerator: 12
      Enter the denominator: 06
      The result of dividing 12.0 by 6.0 is 2.0. 
