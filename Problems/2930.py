e, d = map(int, input().split(" "))

if (d - e) >= 3:
    print("Muito bem! Apresenta antes do Natal!")
elif 0 <= (d - e) < 3:
    print("Parece o trabalho do meu filho!")
    if (d + 2) <= 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")
else:
    print("Eu odeio a professora!")