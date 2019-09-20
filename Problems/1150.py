a = int(input())
x = 0
c = 0
while(True):
    b = int(input())
    if b > a:
        while(x <= b):            
            x += a  
            a += 1
            c += 1
        break

print(c)
        