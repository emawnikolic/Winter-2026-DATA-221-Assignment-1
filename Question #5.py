# Question 5 | Circle Area Comparison with Validation - Write a function that takes the radii of two circles and performs the following:
    # • Validates that both radii are positive integers.
    # • Computes the area of each circle.
    # • Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
# If invalid input is provided, return a meaningful message instead of performing the calculation.

import math

def circle_area_comparison(radius_of_circle_1, radius_of_circle_2):
    if not isinstance(radius_of_circle_1, int) or not isinstance(radius_of_circle_2, int):
        return "Radii must be integers."
    if radius_of_circle_1 <= 0 or radius_of_circle_2 <= 0:
        return "Radii must be positive."

    area1 = math.pi * radius_of_circle_1**2
    area2 = math.pi * radius_of_circle_2**2

    smaller = min(area1, area2)
    larger = max(area1, area2)

    percentage = (smaller / larger) * 100

    return percentage

print(circle_area_comparison(1, 2))