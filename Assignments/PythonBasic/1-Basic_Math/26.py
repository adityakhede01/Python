# 26. How many bricks will be required to lay a path 120 m long and 2.4 m breadth if a brick is 24 cm long and 15 cm wide?

path_length = 12000
path_breadth = 240

brick_length = 24
brick_breadth = 15

brick_area = brick_breadth*brick_length
path_area = path_breadth*path_length

bricks_required = path_area/brick_area

print("Number of bricks required: ", bricks_required)