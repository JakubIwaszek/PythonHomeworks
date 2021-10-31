x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("Point P({0},{1}) is in the first quadrant of the coordinate system".format(x, y))
elif x < 0 and y > 0:
    print("Point P({0},{1}) is in the second quadrant of the coordinate system".format(x, y))
elif x < 0 and y < 0:
    print("Point P({0},{1}) is in the third quadrant of the coordinate system".format(x, y))
elif x > 0 and y < 0:
    print("Point P({0},{1}) is in the fourth quadrant of the coordinate system".format(x, y))