a, b = map(int, input("").split(" "))

if (max(a, b) % min (a, b)) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")