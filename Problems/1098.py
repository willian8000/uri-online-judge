i = 0

for x in range(0, 21, 2):    
    i = x * 0.1
    
    if int(i) == float(i):
        decimal = 0
    else:
        decimal = 1

    for j in range(1, 4):                      
        print('I={0:.{2}f} J={1:.{2}f}'.format(i, j + i, decimal))
    