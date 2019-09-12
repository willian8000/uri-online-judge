lst = []
for x in range(100):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst)) + 1)