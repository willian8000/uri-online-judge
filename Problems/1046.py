a, b = map(int, input("").split(" "))

if a < b:
    print("O JOGO DUROU {} HORA(S)".format(b - a))    
elif a == b:
    print("O JOGO DUROU {} HORA(S)".format(24))    
else: # a > b:
    print("O JOGO DUROU {} HORA(S)".format((24 - a) + b))
    