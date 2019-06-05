total = 0

for x in range(2):
    row = input().split(" ")
    total += int(row[1]) * float(row[2])

print("VALOR A PAGAR: R$ {0:.2f}".format(total))
