# 39. Find the surface of the cylinder if its diameter is 12 centimeters and its height is 9 centimeters.

import math

diameter = 12
height = 9
radius = diameter/2

surface_area_of_cylinder = 2*math.pi*radius*(radius+height)

print(f"Surface are of cylinder: {surface_area_of_cylinder}")