# 3. How many tiles whose length and breadth are 13 cm and 7 cm respectively are needed to cover a rectangular region whose length and breadth are 520 cm and 140 cm?

tile_length = 13
tile_breadth = 7
tile_area = tile_length*tile_breadth

region_length = 520
region_breadth = 140
region_area = region_length*region_breadth

print(f"The number of tiles required are: {region_area/tile_area}")