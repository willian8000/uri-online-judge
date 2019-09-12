for x in range(int(input())):
    v = [float(x) for x in input("").split(" ")]
    print("{:.2}".format((v[0] * .2) + (v[1] * .3) + (v[2] * .5)))
    