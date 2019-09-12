MAX = 10000
n = int(input())

def mod_two(x):
    if x % n == 2:
        print(x)

for x in range(MAX + 1):
    mod_two(x)
