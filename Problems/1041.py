v = str(input("")).split(" ")
x, y = float(v[0]), float(v[1])

if x == y == 0.0:
    print("Origem")
else:
    if x == 0:
        print("Eixo Y")
    elif y == 0:
        print("Eixo X")
    elif x > 0:
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")            
    else:        
        if y > 0:
           print("Q2")
        elif y < 0:
            print("Q3")        
