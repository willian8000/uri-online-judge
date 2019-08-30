a, b, c = map(float, input("").split(" "))

t = [a, b, c]
t.sort(reverse = True)

if t[0] >= t[1] + t[2]:
    print("NAO FORMA TRIANGULO")
else:
    if t[0] ** 2 == t[1] ** 2 + t[2] ** 2:
        print("TRIANGULO RETANGULO")
    if t[0] ** 2 > t[1] ** 2 + t[2] ** 2:
        print("TRIANGULO OBTUSANGULO")
    if t[0] ** 2 < t[1] ** 2 + t[2] ** 2:
        print("TRIANGULO ACUTANGULO")
    if t[0] == t[1] == t[2]:
        print("TRIANGULO EQUILATERO")
    if t[0] == t[1] and t[1] != t[2]:
        print("TRIANGULO ISOSCELES")
    if t[0] != t[1] and t[1] == t[2]:
        print("TRIANGULO ISOSCELES")
