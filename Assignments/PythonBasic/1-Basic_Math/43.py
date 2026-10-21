# 43. Find the cost of polishing the base of a cone whose height is 4cm and slant height 5 cm at the rate of 10 rs. Per sq. cm

import math

height = 4
slant_height_l = 5
rate = 10

radius = ((slant_height_l**2)-(height**2))**0.5
area_of_base_of_cone = math.pi*(radius**2) # Base of cone is a circle
cost = area_of_base_of_cone*rate

print(f"Cost of polishing: {cost}")