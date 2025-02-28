import math

def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    return math.pi * (radius ** 2) 

radius_value = 5

area_result = circle_area(radius_value)

# Print the formatted result
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")
