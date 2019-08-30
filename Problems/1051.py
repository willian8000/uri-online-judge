v = float(input())

def _irrf(v):    
    if v > 4500:            
        print('R$ {:.2f}'.format(350 + ((v - 4500) * 0.28)))
    elif v > 3000:
        print('R$ {:.2f}'.format(80 + ((v - 3000) * 0.18)))
    elif v > 2000:
        print('R$ {:.2f}'.format((v - 2000) * 0.08))        
    else:
        print('Isento')

_irrf(v)