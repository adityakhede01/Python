# 15. Shelly has a rectangular garden of length 22 m and breath 15 m. Her friend Rachel has a square garden of side 21 m. Whose garden is bigger and by how much?

rect_garden_length = 22
rect_garden_breadth = 15
rect_garden_area = rect_garden_length*rect_garden_breadth

square_garden_area = 21**2

if(square_garden_area==rect_garden_area):
    print("Both are equal")
elif(square_garden_area>rect_garden_area):
    print(f"Rachel garden area is bigger by {square_garden_area-rect_garden_area} m")
else:
    print(f"Shelly garden area is bigger by {rect_garden_area-square_garden_area} m")