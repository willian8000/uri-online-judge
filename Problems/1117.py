x = 0
media = 0
while(x < 2):    
    a = float(input())
    if 0 <= a <= 10:
        media += a
        x += 1        
    else:
        print('nota invalida')

print('media = {:.2f}'.format(media / 2))    