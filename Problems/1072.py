_in = 0
qtd = int(input())
for x in range(qtd):
    if int(input()) in range(10, 21):
        _in += 1

print("{0} in\n{1} out".format(_in, qtd - _in))