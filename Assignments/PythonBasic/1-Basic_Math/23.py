# 23. Find the number of cubical boxes of cubical side 3 cm which can be accommodated in carton of dimensions 15 cm × 9 cm × 12 cm.

carton_capacity = 15*9*12
cubical_box_capacity = 3**3

number_of_cubical_boxes = carton_capacity/cubical_box_capacity

print(f"Number of boxes thet can fit: {number_of_cubical_boxes}")