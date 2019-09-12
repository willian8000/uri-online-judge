est = {
    'Inter': 0,
    'Gremio': 0,
    'Empates': 0
}

def final():
    print('{} grenais'.format(est['Inter'] + est['Gremio'] + est['Empates']))
    for key in est:
        print('{0}:{1}'.format(key, est[key]))    
    if est['Inter'] == est['Gremio']:
        print('Nao houve vencedor')
    else:
        print('{} venceu mais'.format(max(est, key=est.get)))
        

def entrada():
    e = 1
    while(e == 1):        
        a, b = map(int, input("").split(" "))
        if a == b:
            est['Empates'] =+ 1
        else:
            est['Inter' if a > b else 'Gremio'] += 1
        
        print('Novo grenal (1-sim 2-nao)')
        e = int(input())
    final()

entrada()
    