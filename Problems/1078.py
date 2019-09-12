def tabuada(n):
    for x in range(1, 11):
        print("{0} x {1} = {2}".format(x, n, x * n))

tabuada(int(input()))