import math
x = int(input())
for _ in range(x):
    n, m = map(int, input().split(" "))
    print(int((math.log10(n**m) +1)))