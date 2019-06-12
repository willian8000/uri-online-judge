for x in range (int(input())):
    n, k = map(int, input().split(" "))
    print(int((n % k) + (n / k)))
