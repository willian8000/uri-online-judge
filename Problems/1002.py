# print("A=" + str(round(float(input())**2 * 3.14159, 4)))  # solution with a single row
n = 3.14159
raio = float(input())
area = round(raio**2 * n, 4)
print('A={0:.4f}'.format(area))
