# 34. A wooded area is in the shape of a a trapezoid whose bases measure 128 m and 92 m and its height is 40 m. A 4 m wide walkway is constructed which runs perpendicular to the two bases. Calculate the area of the wooded area after the addition of the walkway.

base1 = 128
base2 = 92
height = 40

width_of_walkway = 4

area_of_trapezoid = ((base1+base2)/2)*height
area_of_walkway = width_of_walkway*height

final_wooded_area = area_of_trapezoid-area_of_walkway

print(f"Wooded area: {final_wooded_area}")