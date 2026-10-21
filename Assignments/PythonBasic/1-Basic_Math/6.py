# 6. Find the area of a triangle, sides of which are 10 cm and 9 cm and the perimeter 36 cm.

import math

perimeter = 36
side1 = 10
side2 = 9
side3 = perimeter-side1-side2
s= (side1+side2+side3)/2

area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print(f"The area is: {area}")