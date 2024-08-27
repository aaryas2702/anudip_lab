import math

def area_of_triangle(a, b, c):
    """Calculate the area of a triangle using Heron's formula."""
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

# Given sides of the triangle
side1 = 10
side2 = 12
side3 = 14

# Calculate the area
triangle_area = area_of_triangle(side1, side2, side3)

# Print the result
print(f"The area of the triangle with sides {side1}, {side2}, and {side3} is {triangle_area:.2f} square.")

#The area of the triangle with sides 10 cm, 12 cm, and 14 cm is 58.79 square cm.
