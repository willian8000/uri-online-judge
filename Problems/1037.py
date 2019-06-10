value = float(input())

if  0.00 <= value <= 25.00:
    print("Intervalo [0,25]")
elif  25.01 <= value <= 50.00:
    print("Intervalo (25,50]")
elif  50.01 <= value <= 75.00:
    print("Intervalo (50,75]")
elif  70.01 <= value <= 100.00:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")