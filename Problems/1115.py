while(True):
    x, y = map(int, input("").split(" "))

    if min(x, y) == 0:
        break

    if x > 0:
        if y > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if y > 0:   
            print('segundo')
        else:
            print('terceiro')
    