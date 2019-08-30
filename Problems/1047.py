ah, am, bh, bm = map(int, input("").split(" "))

def ret_minutos(am, bm):
    if am < bm:
        return bm - am
    elif am > bm:
        return (60 - am) + bm
    else:
        return 0

def ret_horas(ah, bh):
    if ah < bh:
        if bh - ah == 1 and ret_minutos(am, bm) > 0:
            return 0
        else:
            return bh - ah
    elif ah == bh:
        if ret_minutos(am, bm) > 0:
            if am > bm:
                return 23
            else:
                return 0
        else:
            return 24
    else: # a > b:
        if am > bm:
            return (24 - ah) + bh - 1
        else:
            return (24 - ah) + bh

print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(ret_horas(ah, bh), ret_minutos(am, bm)))
