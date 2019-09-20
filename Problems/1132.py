a, b = int(input()), int(input())
a, b = min(a, b), max(a, b)

# soma de Gauss para os multiplos de 13
# soma de Gauss para todo o 'range'
# subtrai o multiplo de todos

def soma_multiplos(a, b):
    a = a + 13 - (a % 13) if a % 13 != 0 else a
    b = b - (b % 13) if b % 13 != 0 else b
    return int(((a + b) * (((b - a)/13) + 1)) / 2)

def soma(a, b):
    return (((a + b) * ((b - a) + 1)) / 2) - soma_multiplos(a, b)

print(int(soma(a, b)))

