j = 7
for i in range(1, 10, 2):
    for x in range(3):
        print('I={0} J={1}'.format(i, j - x))
    j += 2
