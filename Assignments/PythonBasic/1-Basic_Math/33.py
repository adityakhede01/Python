# 33. A rectangular garden has dimensions of 30 m by 20 m and is divided in to 4 parts by two pathways that run perpendicular from its sides. One pathway has a width of 3m and the other, 4 m. Calculate the total usable area of the garden.

garden_length = 30
garden_width = 20

area_pathway1 = 3*garden_length
area_pathway2 = 4*garden_width

garden_area = garden_length*garden_width
overlaping_area = 3*4
usable_area = garden_area-(area_pathway1+area_pathway2-overlaping_area)

print(f"Usable garden area: {usable_area}")