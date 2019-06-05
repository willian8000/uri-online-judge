def maior(a, b):
    return int((a + b + abs(a - b)) / 2)


row = [int(x) for x in input().split(" ")]
print(str(maior(maior(row[0], row[1]), row[2])) + " eh o maior")
