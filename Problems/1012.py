row =[float(x) for x in input().split(" ")]

print("TRIANGULO: {0:.3f}\n".format((row[0] * row[2]) / 2) +
      "CIRCULO: {0:.3f}\n".format(row[2]**2 * 3.14159) +
      "TRAPEZIO: {0:.3f}\n".format(((row[0] + row[1]) * row[2]) / 2) +
      "QUADRADO: {0:.3f}\n".format(row[1]**2) +
      "RETANGULO: {0:.3f}".format(row[0] * row[1]))
