n = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]


def _notas_(n, notas):
    print(n)
    for div in notas:
        qtd_notas = 0
        if n >= div:
            qtd_notas = int(n / div)
            n -= (qtd_notas * div)

        print(str(qtd_notas) + ' nota(s) de R$ {0},00'.format(div))


_notas_(n, notas)