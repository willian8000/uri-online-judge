# a quantidade de divisores de um número
# é a multiplcação dos expoentes da decomposição do número em primos
# somando 1 para cada elemento
# 15 = 3^1 * 5^1 = 1+1 * 1+1 = 2.2 = 4
divisores = {1: 1, 2: 2}
# lista de primos para decompor
primos = [2]
for x in range(3, 1000, 2):
    div = 0
    for d in range(2, x):
        if x % d == 0:
            div += 1
            break
    if div == 0:
        primos.append(x)


# function to decompose number by primes and return the number of divisors of it
def divisors_number(number):
    divisors = 1
    for div in primos:
        qtd = 0
        while number % div == 0:
            number = number / div
            qtd += 1
        if qtd != 0:
            divisors = (qtd + 1) * divisors
        if number == 1:
            break
    return divisors

#print(divisors_number(5880))
for x in range(1, 10)0:
    numb = 1  # start at 3 because first two values we know
    while True:
        if numb == 100 : break
        if divisors_number(numb) == x and x not in divisores:
            #print(divisores[divisors_number(numb)])
            divisores[x] = numb
            print(divisores)
        numb += 1



