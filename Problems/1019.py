def time_convert(sec, p = ''):
    for t in [3600, 60]:
        if sec >= t:
            x = int(sec / t)
            sec -= x * t
            p += str(x) + ':'
        else:
            p += '0:'
    print(p + str(sec))

time_convert(int(input()))
