row = str(input("")).split(" ")
a, b, c, d = int(row[0]), int(row[1]), int(row[2]), int(row[3])

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")