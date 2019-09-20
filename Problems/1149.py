lst = list([int(x) for x in input().split()])
a, b = lst[0], list(filter(lambda x: (x > 0), lst[1:]))[0]
s = 0
for x in range(b):    
    s += a + x
print(s)