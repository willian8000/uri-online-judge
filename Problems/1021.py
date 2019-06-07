def notas_moedas(n):
    print('NOTAS:')
    for div in [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]:
        qtd_notas = 0
        if n >= div:
            qtd_notas = int(n / div)
            n -= (qtd_notas * div)
        print(str(qtd_notas) + ' nota(s) de R$ {0:.2f}'.format(div))

    print('MOEDAS:')
    for div in [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]:
        qtd_moedas = 0
        if n >= div:
            qtd_moedas= int(n / div)
            n = round(n - (qtd_moedas * div), 2)
        print(str(qtd_moedas) + ' moeda(s) de R$ {0:.2f}'.format(div))


notas_moedas(float(input()))