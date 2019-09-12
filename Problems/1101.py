while(True):
    a, b = map(int, input("").split(" "))
    a, b = min(a, b), max(a, b)
    if a <= 0:
        break
        
    # s = sum(x for x in range(min(a, b), max(a, b + 1)))
    # O(n)
    # forma de gauss, onde s = n * (n + 1) / 2
    # O(1)
    s = ((b * (b + 1)) - (a * (a - 1))) / 2
    x = list(x for x in range (a, b + 1))
    print(' '.join(map(str, x)), 'Sum={}'.format(int(s)))
    