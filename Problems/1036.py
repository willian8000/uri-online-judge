import math
a, b, c = map(float, input("").split(" "))

if a != 0.00:
    try:
        delta = math.sqrt(b**2 - (4 * a * c))
        R1 = (-b + delta) / (2 * a)
        R2 = (-b - delta) / (2 * a)

        print("R1 = {0:.5f}\nR2 = {1:.5f}".format(R1, R2))
    except Exception as error:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
