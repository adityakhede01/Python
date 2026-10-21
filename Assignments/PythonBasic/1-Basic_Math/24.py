# 24. How many bricks each 25 cm long, 10 cm wide and 7.5 cm thick will be required for a wall 20 m long, 2 m high and 0.75 m thick? If bricks sell at $900 per thousand what will it cost to build the wall?

brick_length = 25
brick_width = 10
brick_height = 7.5

wall_length = 2000
wall_height = 200
wall_width = 75

cost_of_brick_per_1000 = 900
cost_of_single_brick = cost_of_brick_per_1000/1000

brick_volume = brick_length*brick_width*brick_height
wall_volume = wall_length*wall_width*wall_height

no_of_brick_for_wall = wall_volume/brick_volume

total_cost = no_of_brick_for_wall*cost_of_single_brick

print(f"The total cost for the wall will be: {int(total_cost)}$")