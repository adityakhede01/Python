# 37. The surface of the cylinder is 149 cm². The cylinder height is 6 cm. What is the diameter of this cylinder?

# Taking surface as curved surface area

import math

curved_surface_area = 149
height = 6

diameter = curved_surface_area/(math.pi*height)

print(f"Diameter: {diameter} cm")