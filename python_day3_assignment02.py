Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Take input from the user
... num1 = int(input("Enter the first number: "))
... num2 = int(input("Enter the second number: "))
... 
... # Display numbers before swapping
... print(f"Before swapping: num1 = {num1}, num2 = {num2}")
... 
... # Swapping using tuple unpacking
... num1, num2 = num2, num1
... 
... # Display numbers after swapping
... print(f"After swapping: num1 = {num1}, num2 = {num2}")
... 
... First number: 3
... Second number: 5
... 
... # output num1 = 5, num2 = 3
