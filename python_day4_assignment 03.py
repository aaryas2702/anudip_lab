def is_leap_year(year):
    """
    Determine whether a given year is a leap year.
    
    Parameters:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()
#output
    Enter a year: 2024
    2024 is a leap year.

   Enter a year: 1997
   1997 is not a leap year. 
