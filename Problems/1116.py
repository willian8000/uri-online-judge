for x in range(int(input())):
    a, b = map(int, input("").split(" "))

    try:
        print('{:.1f}'.format(a / b))
    except Exception as e:
        print('divisao impossivel')