# 29. How many square tiles of side 10 cm will be required to tile a floor measuring 800 cm by 900 cm?

square_tile_side = 10

floor_length = 800
floor_width = 900

tile_area = 4*(square_tile_side)
floor_area = floor_length*floor_width
no_of_tiles = floor_area/tile_area

print(f"Number of Tiles required: {no_of_tiles}")