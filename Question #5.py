# Question 5 | Circle Area Comparison with Validation - Write a function that takes the radii of two circles and performs the following:
    # • Validates that both radii are positive integers.
    # • Computes the area of each circle.
    # • Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
# If invalid input is provided, return a meaningful message instead of performing the calculation.

import math

def circle_area_comparison(r1, r2):
    if not isinstance(r1, int) or not isinstance(r2, int):
        return "Radii must be integers."
    if r1 <= 0 or r2 <= 0:
        return "Radii must be positive."

    area1 = math.pi * r1**2
    area2 = math.pi * r2**2

    smaller = min(area1, area2)
    larger = max(area1, area2)

    percentage = (smaller / larger) * 100

    return percentage

print(circle_area_comparison(1, 2))