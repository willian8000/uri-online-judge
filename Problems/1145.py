a, b = map(int, input().split())
i = 1

for x in range(1, int((b / a)) + 1):    
    s = ''
    for _ in range(a):        
        s += str(i) + ' '
        i += 1
    print(s[:-1])
 