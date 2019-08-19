a, b, c = map(float, input("").split(" "))

# conditions for the exists triangle
# um dos lados deve ser maior que o valor absoluto 
# da diferença dos outros dois lado e menor que a 
# a somo dos outros dois lados

if (abs(b - c) < a < b + c and 
    abs(a - c) < b < a + c and
    abs(a - b) < c < a + b):
    print("Perimetro = {}".format(a + b + c))
else:
    print("Area = {}".format(((a + b) * c) / 2))
