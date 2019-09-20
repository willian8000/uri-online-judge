a, b = int(input()), int(input())
a, b = min(a, b), max(a, b)

for x in range(a + 1, b):
    if x % 5 in (2, 3):
        print(x)
