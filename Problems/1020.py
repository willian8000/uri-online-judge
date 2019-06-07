def idade_dias(dias):
    for d, v in {'ano(s)': 365, 'mes(es)': 30}.items():
        x = int(dias / v)
        dias -= x * v
        print(int(x), d)
    print(int(dias), 'dia(s)')


idade_dias(int(input()))
