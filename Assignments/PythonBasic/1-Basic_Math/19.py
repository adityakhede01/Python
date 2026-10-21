# 19. A cube with an edge of 7 cm and a cuboid measuring 7 cm × 4 cm × 8 am are kept on a table. Which shape has more volume?

cube_edge = 7
cube_volume = cube_edge**3

cuboid_volume = 7*4*8

if(cube_volume==cuboid_volume):
    print("Equal volume")
elif(cube_volume>cuboid_volume):
    print("Cube has more volume.")
else:
    print("Cuboid has more volume.")