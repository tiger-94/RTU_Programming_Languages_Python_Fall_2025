"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

# Import math module
import math

def circle_area(radius):
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2

if __name__ == "__main__":
    # Ask for user input
    radius_input = float(input("Enter the radius of the circle: "))
    area = circle_area(radius_input)
    print(f"Area of the circle: {area:.2f}")
