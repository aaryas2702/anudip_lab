# Function to determine the largest of three numbers
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Main function to handle user input and call find_largest function
def main():
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        # Find the largest number and print the result
        largest = find_largest(num1, num2, num3)
        print(f"The largest number is: {largest}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the main function
if __name__ == "__main__":
    main()
# output
  Enter the first number: 8
  Enter the second number: 7
  Enter the third number: 6
  The largest number is: 8.0
