a = float(input())

if 0 < a <= 400:
    print("Novo salario: {:.2f}".format(a * 1.15))
    print("Reajuste ganho: {:.2f}".format(a * 0.15))
    print("Em percentual: {} %".format(15))
elif 400 < a <= 800:
    print("Novo salario: {:.2f}".format(a * 1.12))
    print("Reajuste ganho: {:.2f}".format(a * 0.12))
    print("Em percentual: {} %".format(12))
elif 800 < a <= 1200:
    print("Novo salario: {:.2f}".format(a * 1.10))
    print("Reajuste ganho: {:.2f}".format(a * 0.10))
    print("Em percentual: {} %".format(10))
elif 1200 < a <= 2000:
    print("Novo salario: {:.2f}".format(a * 1.07))
    print("Reajuste ganho: {:.2f}".format(a * 0.07))
    print("Em percentual: {} %".format(7))
else:
    print("Novo salario: {:.2f}".format(a * 1.04))
    print("Reajuste ganho: {:.2f}".format(a * 0.04))
    print("Em percentual: {} %".format(4))