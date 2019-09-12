def _nota():
    while(True):
        a = float(input())
        if 0 <= a <= 10:
            return a
        else:
            print('nota invalida')

def _media():
    media = 0
    x = 0
    while(x < 2):        
        media += _nota()
        x += 1                
    return media / 2

def main():
    a = 1
    while(True):        
        if a == 1:
            print('media = {:.2f}'.format(_media()))
            print('novo calculo (1-sim 2-nao)')
            pass
        elif a == 2:
            break
        else:
            print('novo calculo (1-sim 2-nao)')
            pass
        a = int(input())

main()