"""
Lab 3.2 – Comprehensions and Transformations

Goals:
- Practice list, set, and dictionary comprehensions.
- Transform and filter data concisely.
"""


numbers = [3, 8, -2, 7, 0, -5, 10]


squares = [x**2 for x in numbers]

positives = [x for x in numbers if x > 0]


even_squares = {x**2 for x in numbers if x % 2 == 0}


cubes = {x: x**3 for x in numbers}


print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
