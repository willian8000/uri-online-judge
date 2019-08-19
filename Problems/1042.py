row = str(input("")).split(" ")
row_sort = [int(row[0]), int(row[1]), int(row[2])]
row_sort.sort()

for value in row_sort:
    print(value)

print('')

for value in row:
    print(value)