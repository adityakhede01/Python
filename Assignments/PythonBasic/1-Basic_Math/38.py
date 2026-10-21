# 38. The cylinder has a volume of 1287. The base has a radius 10. What is the area of the surface of the cylinder?

import math

volume_of_cylinder = 1287
radius = 10

height = volume_of_cylinder/(math.pi*(radius**2))
surface_area = 2*math.pi*radius*(radius+height)

print(f"Surface area of cylinder: {surface_area}")