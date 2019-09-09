v = []
v.append(int(input()))
v.append(int(input()))

if min(v) % 2 != 0:
    v_min = min(v) + 2
else:
    v_min = min(v) + 1

x = list(range(v_min, max(v), 2))
print(sum(x))