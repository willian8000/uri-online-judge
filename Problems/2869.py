# a quantidade de divisores de um número
# é a multiplcação dos expoentes da decomposição do número em primos
# somando 1 para cada elemento
# 15 = 3^1 * 5^1 = 1+1 * 1+1 = 2.2 = 4
divisores = {1: 1, 2: 2, 3: 4, 4: 6}
aux = {}
primos = [2]
for x in range(3, 10000, 2):
    div = 0
    for d in range(2, x):
        if x % d == 0:
            div += 1
            break
    if div == 0:
        primos.append(x)


# function to decompose number by primes and return the number of divisors of it
def divisor(number):
    result = 1
    for div in primos:
        qtd = 0
        while number % div == 0:
            number = number / div
            qtd += 1
        if qtd != 0:
            result *= (qtd + 1)
        if number == 1:
            return result


n = 2
while True:
    x = divisor(n)
    aux[n] = x
    if x not in divisores:
        divisores[x] = n
        print(x, n)
    n += 2