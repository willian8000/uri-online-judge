a = 1

def s(b):
    global a
    a += b
    return a - b

def msg():
    a = int(input())
    for _ in range(a):
        print('{0} {1} {2} PUM'.format(s(1), s(1), s(2)))

msg()