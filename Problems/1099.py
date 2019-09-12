def odd_sum():    
    a, b = map(int, input("").split(" "))
    a, b = min(a, b), max(a, b)   

    a += 2 if a % 2 == 1 else 1
    lst = [int(x) for x in range(a, b, 2)]    

    print(sum(lst))

for x in range(int(input())):
    odd_sum()
