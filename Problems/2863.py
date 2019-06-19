while True:
    try:
        a = 12
        for _ in range(int(input())):
            b = float(input())
            if b < a:
                a = b
        print(a)
    except:
        break
