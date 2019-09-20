def entrada():    
    a = int(input())
    exit() if a == 0 else True
    
    s = ''    
    for x in range(1, a + 1):
        s += (str(x) + ' ')
    print(s[:-1])

while(True):
    entrada()
