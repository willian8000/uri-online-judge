dic = [0, 0, 0]

def msg_fim():
    print('MUITO OBRIGADO')
    print('Alcool: {}'.format(dic[0]))
    print('Gasolina: {}'.format(dic[1]))
    print('Diesel: {}'.format(dic[2]))
    exit()

def entrada():
    a = int(input())
    if 1 <= a <= 3:
        valida_entrada(a, dic)
    msg_fim() if a == 4 else entrada()

def valida_entrada(a, b):
    b[a - 1] += 1

while(True):
    entrada()
    

