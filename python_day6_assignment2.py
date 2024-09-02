2. Write a python program finding the factorial of a given number using a while loop
def factorial(n):
    # Initialize the result to 1
    result = 1
    
    # While loop to calculate the factorial
    while n > 0:
        result *= n
        n -= 1
    
    return result

# Input from the user
try:
    num = int(input("Enter a number to find its factorial: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {num} is {factorial(num)}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    
#output
    Enter a number to find its factorial: 8
The factorial of 8 is 40320.
