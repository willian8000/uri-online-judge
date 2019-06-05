import math

xy_1 = [float(x) for x in input().split(" ")]
xy_2 = [float(x) for x in input().split(" ")]

print("{0:.4f}".format(math.sqrt((xy_2[0] - xy_1[0])**2 + (xy_2[1] - xy_1[1])**2)))
