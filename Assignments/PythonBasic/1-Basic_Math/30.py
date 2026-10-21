# 30. How many tiles of length 5 cm and breadth 8 cm are needed to tile the floor of a bed room 200 cm long and 400 cm wide?

tile_length = 5
tile_width = 8

floor_length = 200
floor_width = 400

no_of_tiles = (floor_length*floor_width)/(tile_length*tile_width)

print(f"Number of Tiles required: {no_of_tiles}")