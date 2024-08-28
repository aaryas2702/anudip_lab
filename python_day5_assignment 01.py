def div(num1, num2):
    # Check if the second number is zero to avoid division by zero
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        # Perform the division
        result = num1 / num2
        return result

# Call the function with two numbers
number1 = 5
number2 = 8
result = div(number1, number2)

# Display the result
print(f"The result of dividing {number1} by {number2} is {result}")

#output
The result of dividing 5 by 8 is 0.625
