import math

a, b, c, d = map(float, input("").split(" "))
media = round((a * 0.2) + (b * 0.3) + (c * 0.4) + (d * 0.1), 2)

def truncate(f):
    return math.floor(f * 10 ** 1) / 10 ** 1

if media >= 7.0:
    print("Media: {0}".format(truncate(media)))
    print("Aluno aprovado.")        
elif 5 <= media < 7.0:
    print("Media: {0}".format(truncate(media)))
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: {0}".format(e))
    media = (media + e) / 2.0
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {0}".format(truncate(media)))
else:
    print("Media: {0}".format(truncate(media)))
    print("Aluno reprovado.")
