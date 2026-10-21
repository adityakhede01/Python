# 9. Find the area of an equilateral triangle, the length of whose sides is 12 cm.

import math

side =12
s= (side+side+side)/2

area = math.sqrt(s*(s-side)*(s-side)*(s-side))

print(f"Area: {area}")