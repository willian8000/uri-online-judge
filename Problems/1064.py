p = 0
soma = []

for x in range (6):               
    a = float(input())
    if a >= 0:
        soma.append(a)
        p += 1        
    
print('{0} valores positivos\n{1:.2}'.format(p, sum(soma) / p))
